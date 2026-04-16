import os
import vtracer
from PIL import Image, ImageDraw, ImageFont
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ambil API Key dari environment variable atau ganti string di bawah
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "MASUKKAN_API_KEY_ANDA_DISINI")

if GEMINI_API_KEY != "MASUKKAN_API_KEY_ANDA_DISINI":
    genai.configure(api_key=GEMINI_API_KEY)

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r") as f:
        return f.read()

@app.get("/api/generate")
async def generate(prompt: str):
    try:
        # Optimasi prompt untuk kebutuhan tracing vektor yang solid
        full_prompt = f"{prompt}, flat vector art style, solid shapes, isolated on white background, sharp clean lines, no photo realism, no complex gradients"
        
        raster_path = "input.png"
        svg_path = "output.svg"

        if GEMINI_API_KEY == "MASUKKAN_API_KEY_ANDA_DISINI":
            # Jika API Key belum diatur, buat gambar dummy dengan teks untuk dites
            img = Image.new('RGB', (512, 512), color = (255, 255, 255))
            d = ImageDraw.Draw(img)
            d.rectangle([100, 100, 412, 412], fill=(255, 200, 0), outline=(0, 0, 0), width=5)
            img.save(raster_path)
            print("API Key belum diatur. Menggunakan gambar dummy.")
        else:
            # Implementasi pemanggilan model Imagen / Gemini untuk gambar
            # Pastikan model yang dipanggil sesuai dengan akses API Anda (misal: imagen-3.0-generate-001)
            model = genai.ImageGenerationModel("imagen-3.0-generate-001")
            result = model.generate_images(
                prompt=full_prompt,
                number_of_images=1,
                aspect_ratio="1:1",
                output_mime_type="image/png"
            )
            result.images[0].image.save(raster_path)

        # Proses mengubah Raster menjadi Vektor SVG
        vtracer.convert_image_to_svg(
            raster_path, 
            svg_path,
            colortype='color',
            mode='spline',
            filter_speckle=4,
            color_precision=6,
            layer_difference=16
        )

        return {"message": "Success", "vector_url": "/api/download"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/download")
async def download():
    return FileResponse("output.svg", media_type="image/svg+xml", filename="senaqo_vector.svg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
