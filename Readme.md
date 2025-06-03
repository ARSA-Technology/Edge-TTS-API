# ARSA Edge-TTS API 🎤

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)

**Professional Indonesian Text-to-Speech API** built by [ARSA Technology](https://arsa.technology) using Microsoft Edge TTS.

Perfect for content creators, developers, and businesses needing high-quality Indonesian voice synthesis for videos, applications, and automation workflows.

## ✨ Features

🇮🇩 **Native Indonesian Support** - Natural sounding Indonesian voices (female & male)  
🇺🇸 **English Support** - Professional US English voices  
🚀 **High Performance** - Fast generation with concurrent request handling  
📦 **Batch Processing** - Generate multiple audio files simultaneously  
🔄 **Auto Cleanup** - Automatic file management and cleanup  
📊 **Analytics** - Built-in statistics and monitoring  
🐳 **Docker Ready** - One-command deployment  
🌐 **Remote Access** - API accessible from anywhere  
📖 **Interactive Docs** - Auto-generated API documentation  
🏥 **Health Monitoring** - Built-in health checks and status monitoring  

## 🎯 Use Cases

- **Video Content Creation** - Generate narration for educational videos
- **E-Learning Platforms** - Create course audio in Indonesian
- **Marketing Automation** - Automated voice-overs for social media
- **Accessibility Tools** - Text-to-speech for Indonesian applications
- **IoT & AI Projects** - Voice responses for smart devices
- **Content Localization** - Convert text content to Indonesian audio

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
git clone https://github.com/arsa-technology/edge-tts-api.git
cd edge-tts-api
docker-compose up -d
```

### Option 2: Docker Run

```bash
docker run -d \
  --name arsa-edge-tts \
  -p 8021:8021 \
  -v $(pwd)/output:/app/output \
  arsa/edge-tts-api:latest
```

### Option 3: Local Development

```bash
git clone https://github.com/arsa-technology/edge-tts-api.git
cd edge-tts-api
pip install -r requirements.txt
python main.py
```

## 🎤 Available Voices

| Voice ID | Language | Gender | Description |
|----------|----------|--------|-------------|
| `female` | Indonesian | Female | Professional, clear pronunciation |
| `male` | Indonesian | Male | Authoritative, business tone |
| `female_us` | English | Female | Natural US English |
| `male_us` | English | Male | Professional US English |

## 📡 API Usage

### Basic Indonesian TTS

```bash
curl -X POST http://localhost:8021/tts \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Selamat datang di ARSA Technology, perusahaan AI terdepan di Indonesia",
    "voice": "female",
    "language": "indonesian"
  }'
```

### Advanced Parameters

```bash
curl -X POST http://localhost:8021/tts \
  -H "Content-Type: application/json" \
  -d '{
    "text": "ARSA Technology menghadirkan solusi AI dengan akurasi 99,67 persen",
    "voice": "female",
    "rate": "+15%",
    "pitch": "+30Hz",
    "volume": "+10%",
    "language": "indonesian",
    "output_format": "wav"
  }'
```

### Batch Processing

```bash
curl -X POST http://localhost:8021/tts/batch \
  -H "Content-Type: application/json" \
  -d '[
    {
      "text": "Selamat pagi, Indonesia!",
      "voice": "female",
      "language": "indonesian"
    },
    {
      "text": "Good morning, world!",
      "voice": "female_us", 
      "language": "english"
    }
  ]'
```

### Python Integration

```python
import requests

# Generate Indonesian speech
response = requests.post('http://localhost:8021/tts', json={
    "text": "Teknologi AI untuk masa depan Indonesia",
    "voice": "female",
    "rate": "+10%",
    "language": "indonesian"
})

result = response.json()
if result["success"]:
    # Download the audio file
    audio_response = requests.get(f"http://localhost:8021{result['audio_url']}")
    with open("output.wav", "wb") as f:
        f.write(audio_response.content)
```

### JavaScript/Node.js Integration

```javascript
const axios = require('axios');
const fs = require('fs');

async function generateIndonesianTTS() {
  try {
    // Generate speech
    const response = await axios.post('http://localhost:8021/tts', {
      text: 'ARSA Technology menghadirkan inovasi AI terdepan',
      voice: 'female',
      rate: '+10%',
      language: 'indonesian'
    });

    if (response.data.success) {
      // Download audio
      const audioResponse = await axios.get(
        `http://localhost:8021${response.data.audio_url}`,
        { responseType: 'arraybuffer' }
      );
      
      fs.writeFileSync('output.wav', audioResponse.data);
      console.log('Audio generated successfully!');
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

generateIndonesianTTS();
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `TTS_MAX_TEXT_LENGTH` | `5000` | Maximum characters per request |
| `TTS_CLEANUP_INTERVAL` | `3600` | File cleanup interval (seconds) |
| `PYTHONUNBUFFERED` | `1` | Python output buffering |

### Docker Compose Configuration

```yaml
version: '3.8'
services:
  edge-tts:
    build: .
    ports:
      - "8021:8021"
    environment:
      - TTS_MAX_TEXT_LENGTH=5000
      - TTS_CLEANUP_INTERVAL=3600
    volumes:
      - ./output:/app/output
    restart: unless-stopped
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/` | GET | Service information |
| `/health` | GET | Health check |
| `/voices` | GET | List available voices |
| `/tts` | POST | Generate single audio |
| `/tts/batch` | POST | Generate multiple audios |
| `/audio/{audio_id}` | GET | Download audio file |
| `/stats` | GET | Service statistics |
| `/docs` | GET | Interactive API documentation |

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Test locally
python test_client.py

# Test remote server
python test_client.py YOUR_SERVER_IP

# Expected output:
# ✅ Health Check: healthy
# ✅ Voice Listing: 4 voices available
# ✅ Indonesian TTS: Generated successfully
# ✅ English TTS: Generated successfully
# ✅ Batch TTS: 3/3 successful
# ✅ Service Stats: All metrics available
```

## 🌐 Remote Access Setup

### 1. Open Firewall Ports

```bash
# Ubuntu/Debian
sudo ufw allow 8021/tcp

# CentOS/RHEL
sudo firewall-cmd --permanent --add-port=8021/tcp
sudo firewall-cmd --reload
```

### 2. Cloud Provider Configuration

**AWS Security Group:**
```
Type: Custom TCP
Port: 8021
Source: 0.0.0.0/0 (or specific IPs)
```

**Google Cloud Firewall:**
```bash
gcloud compute firewall-rules create edge-tts-api \
  --allow tcp:8021 \
  --source-ranges 0.0.0.0/0
```

### 3. Nginx Reverse Proxy (Optional)

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location /api/tts/ {
        proxy_pass http://localhost:8021/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 📈 Performance & Limitations

### Performance Metrics
- **Generation Speed**: ~2-5 seconds per 100 words
- **Concurrent Requests**: Handles multiple simultaneous requests
- **Memory Usage**: ~100-200MB per container
- **File Size**: ~1MB per minute of audio (WAV format)

### Rate Limits
- **Text Length**: Max 5,000 characters per request
- **Batch Size**: Max 10 requests per batch
- **File Retention**: Auto-cleanup after 1 hour

### Supported Formats
- **Output**: WAV (default), MP3
- **Sample Rate**: 22kHz (Edge TTS default)
- **Channels**: Mono
- **Bit Depth**: 16-bit

## 🛠️ Development

### Project Structure
```
edge-tts-service/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Container configuration
├── docker-compose.yml  # Service orchestration
├── test_client.py      # Test suite
├── .env               # Environment variables
└── output/            # Generated audio files
```

### Local Development

```bash
# Clone repository
git clone https://github.com/arsa-technology/edge-tts-api.git
cd edge-tts-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload --host 0.0.0.0 --port 8021
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔒 Security Considerations

### Production Deployment
- **Authentication**: Add API key authentication for production
- **Rate Limiting**: Implement request rate limiting
- **Input Validation**: Sanitize text input
- **Network Security**: Use HTTPS and restrict access by IP
- **Resource Limits**: Set container memory/CPU limits

### Docker Security
```yaml
# Example production configuration
services:
  edge-tts:
    build: .
    user: "1000:1000"  # Non-root user
    read_only: true    # Read-only filesystem
    tmpfs:
      - /tmp:rw,noexec,nosuid,size=100m
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '1.0'
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support & Community

### Get Help
- 📖 **Documentation**: [API Docs](http://localhost:8021/docs)
- 🐛 **Issues**: [GitHub Issues](https://github.com/arsa-technology/edge-tts-api/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/arsa-technology/edge-tts-api/discussions)

### Commercial Support
For enterprise support, custom development, or consulting services:
- 🌐 **Website**: [arsa.technology](https://arsa.technology)
- 📧 **Email**: [support@arsa.technology](mailto:support@arsa.technology)
- 📱 **WhatsApp**: [Contact Us](https://wa.me/6282145676433)

## 🏢 About ARSA Technology

**ARSA Technology** is Indonesia's leading AI and IoT solutions provider, specializing in:
- 🤖 **Artificial Intelligence** - Face recognition, computer vision, NLP
- 🌐 **Internet of Things** - Industrial monitoring, smart city solutions
- 🏭 **Industry 4.0** - Manufacturing automation and optimization
- 🏥 **Digital Health** - Medical AI and self-service health platforms
- 🎓 **Virtual Reality** - Immersive training and simulation

**Trusted by**: Ministry of Defense of Indonesia, Indonesian National Police, and leading enterprises across Southeast Asia.

### Our Products
- **ARSACA**: Advanced vision AI analytics for human recognition and safety
- **AKSAYANA**: Vehicle analytics and license plate recognition
- **SYNAPTA**: Medical AI platform for diagnostics and health monitoring
- **ANIYATA**: VR solutions for industrial training and simulation

## 🌟 Showcase

### Real-World Implementations

**Video Content Creation**
```python
# Generate educational content in Indonesian
educational_script = """
Teknologi AI ARSA telah membantu berbagai industri di Indonesia. 
Dengan akurasi 99,67 persen dalam pengenalan wajah, 
sistem kami mengamankan fasilitas strategis negara.
"""

tts_response = requests.post('http://localhost:8021/tts', json={
    "text": educational_script,
    "voice": "female",
    "rate": "+10%",
    "language": "indonesian"
})
```

**Multilingual Content**
```python
# Create bilingual content for international audience
contents = [
    {
        "text": "Selamat datang di masa depan teknologi Indonesia",
        "voice": "female",
        "language": "indonesian"
    },
    {
        "text": "Welcome to the future of Indonesian technology", 
        "voice": "female_us",
        "language": "english"
    }
]

batch_response = requests.post('http://localhost:8021/tts/batch', json=contents)
```

## 🚀 Roadmap

### Current Version (v1.0)
- ✅ Indonesian and English TTS
- ✅ Batch processing
- ✅ Docker deployment
- ✅ Remote access
- ✅ Auto cleanup

### Upcoming Features (v1.1)
- 🔄 **Regional Indonesian Dialects** - Javanese, Sundanese voices
- 🔑 **API Authentication** - JWT token support
- 📊 **Advanced Analytics** - Usage metrics and reporting
- 🎛️ **Voice Customization** - Emotion and style controls
- 📱 **Mobile SDK** - iOS and Android libraries

### Future Releases (v2.0+)
- 🧠 **AI Voice Cloning** - Custom voice training
- 🎵 **SSML Support** - Advanced speech markup
- ☁️ **Cloud Integration** - AWS, GCP, Azure deployments
- 🔄 **Real-time Streaming** - Live TTS streaming

---

<div align="center">

**Made with ❤️ by ARSA Technology**

[🌐 Website](https://arsa.technology) • [📧 Email](mailto:hello@arsa.technology) • [📱 WhatsApp](https://wa.me/6285168623493)

⭐ **Star this repository if it helped you!** ⭐

</div>