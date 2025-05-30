from fastapi import FastAPI, HTTPException
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulated Gemini AI responses
def generate_gemini_response(user_message: str) -> str:
    user_message = user_message.lower()
    
    if "halo" in user_message or "hai" in user_message:
        return "Halo! Saya Asisten AI Paket Pro Atur Aja. Ada yang bisa saya bantu?"
    elif "fitur" in user_message:
        return "Paket Pro menyediakan fitur AI eksklusif untuk analisis bisnis, prediksi keuangan, dan otomatisasi tugas. Apakah Anda ingin detail lebih lanjut?"
    elif "harga" in user_message or "biaya" in user_message:
        return "Paket Pro tersedia mulai dari Rp 150.000/bulan dengan fitur AI Gemini untuk kebutuhan bisnis Anda."
    elif "terima kasih" in user_message:
        return "Sama-sama! Saya siap membantu Anda kapan saja 😊"
    else:
        return "Saya sedang memproses permintaan Anda... (simulasi respons AI Gemini)"

@app.post("/api/chat")
async def chat_endpoint(data: dict):
    try:
        user_message = data.get("message", "")
        if not user_message:
            raise HTTPException(status_code=400, detail="Pesan tidak boleh kosong")
        
        response = generate_gemini_response(user_message)
        return {"response": response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("backend_api:app", host="0.0.0.0", port=5000, reload=True)