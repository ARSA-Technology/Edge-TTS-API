#!/usr/bin/env python3
"""
Test client for ARSA Technology Edge-TTS API
Usage: python test_client.py [SERVER_IP]
"""

import requests
import json
import sys
import time
from pathlib import Path

def get_api_base():
    """Get API base URL from command line or prompt"""
    if len(sys.argv) > 1:
        server_ip = sys.argv[1]
    else:
        server_ip = input("Enter server IP (or press Enter for localhost): ").strip()
        if not server_ip:
            server_ip = "localhost"
    
    return f"http://{server_ip}:8021"

def test_health(api_base):
    """Test API health"""
    try:
        print("🔍 Testing health check...")
        response = requests.get(f"{api_base}/health", timeout=10)
        response.raise_for_status()
        result = response.json()
        print(f"✅ Health: {result['status']} - {result['timestamp']}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_voices(api_base):
    """Test voice listing"""
    try:
        print("🎤 Testing voice listing...")
        response = requests.get(f"{api_base}/voices", timeout=10)
        response.raise_for_status()
        voices = response.json()
        
        print("✅ Available voices:")
        for voice in voices:
            print(f"   {voice['voice_id']}: {voice['description']} ({voice['language']})")
        
        return True
    except Exception as e:
        print(f"❌ Voice listing failed: {e}")
        return False

def test_indonesian_tts(api_base):
    """Test Indonesian TTS generation"""
    try:
        print("🇮🇩 Testing Indonesian TTS...")
        
        request_data = {
            "text": "Selamat datang di ARSA Technology. Kami adalah perusahaan AI dan IoT terdepan di Indonesia yang menghadirkan solusi teknologi canggih dengan akurasi tinggi untuk transformasi digital bisnis Anda.",
            "voice": "female",
            "rate": "+15%",
            "pitch": "+30Hz",
            "language": "indonesian",
            "output_format": "wav"
        }
        
        print("   Generating speech...")
        response = requests.post(f"{api_base}/tts", json=request_data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if result["success"]:
            print(f"✅ Indonesian TTS generated:")
            print(f"   Audio ID: {result['audio_id']}")
            print(f"   Duration: {result['duration_estimate']}s")
            print(f"   Voice: {result['voice_used']}")
            print(f"   File size: {result['file_size']} bytes")
            
            # Download the audio file
            print("   Downloading audio...")
            audio_url = f"{api_base}{result['audio_url']}"
            audio_response = requests.get(audio_url, timeout=30)
            audio_response.raise_for_status()
            
            filename = f"test_indonesian_{result['audio_id']}.wav"
            Path(filename).write_bytes(audio_response.content)
            print(f"💾 Audio saved as: {filename}")
            
            return True
        else:
            print(f"❌ TTS failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Indonesian TTS failed: {e}")
        return False

def test_english_tts(api_base):
    """Test English TTS generation"""
    try:
        print("🇺🇸 Testing English TTS...")
        
        request_data = {
            "text": "Welcome to ARSA Technology. We are Indonesia's leading AI and IoT company, providing cutting-edge technology solutions with 99.67% accuracy in face recognition and comprehensive IoT monitoring systems.",
            "voice": "female_us",
            "rate": "+10%",
            "language": "english",
            "output_format": "wav"
        }
        
        print("   Generating speech...")
        response = requests.post(f"{api_base}/tts", json=request_data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if result["success"]:
            print(f"✅ English TTS generated:")
            print(f"   Audio ID: {result['audio_id']}")
            print(f"   Duration: {result['duration_estimate']}s")
            print(f"   Voice: {result['voice_used']}")
            
            # Download the audio file
            audio_url = f"{api_base}{result['audio_url']}"
            audio_response = requests.get(audio_url, timeout=30)
            audio_response.raise_for_status()
            
            filename = f"test_english_{result['audio_id']}.wav"
            Path(filename).write_bytes(audio_response.content)
            print(f"💾 Audio saved as: {filename}")
            
            return True
        else:
            print(f"❌ English TTS failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ English TTS failed: {e}")
        return False

def test_batch_tts(api_base):
    """Test batch TTS generation"""
    try:
        print("📦 Testing batch TTS...")
        
        batch_requests = [
            {
                "text": "ARSA Technology menghadirkan solusi AI terdepan untuk industri Indonesia.",
                "voice": "female",
                "language": "indonesian"
            },
            {
                "text": "Teknologi pengenalan wajah dengan akurasi 99 koma 67 persen.",
                "voice": "male", 
                "language": "indonesian"
            },
            {
                "text": "IoT sensors for smart manufacturing and predictive maintenance.",
                "voice": "female_us",
                "language": "english"
            }
        ]
        
        print("   Processing batch...")
        response = requests.post(f"{api_base}/tts/batch", json=batch_requests, timeout=60)
        response.raise_for_status()
        result = response.json()
        
        if result["batch_success"]:
            print(f"✅ Batch TTS completed:")
            print(f"   Total requests: {result['total_requests']}")
            print(f"   Successful: {result['successful']}")
            print(f"   Failed: {result['failed']}")
            
            for i, res in enumerate(result['results']):
                if res.get('success'):
                    print(f"   {i+1}. ✅ {res['text_preview']}")
                else:
                    print(f"   {i+1}. ❌ {res['text_preview']} - {res.get('error', 'Unknown error')}")
            
            return True
        else:
            print(f"❌ Batch TTS failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Batch TTS failed: {e}")
        return False

def test_stats(api_base):
    """Test service statistics"""
    try:
        print("📊 Testing service statistics...")
        response = requests.get(f"{api_base}/stats", timeout=10)
        response.raise_for_status()
        stats = response.json()
        
        print("✅ Service statistics:")
        print(f"   Audio files: {stats['total_audio_files']}")
        print(f"   Total size: {stats['total_size_mb']} MB")
        print(f"   Available voices: {stats['available_voices']}")
        print(f"   Max text length: {stats['max_text_length']} chars")
        print(f"   Cleanup interval: {stats['cleanup_interval_hours']} hours")
        
        return True
    except Exception as e:
        print(f"❌ Stats test failed: {e}")
        return False

def main():
    print("🎬 ARSA Technology Edge-TTS API Test Suite")
    print("=" * 50)
    
    api_base = get_api_base()
    print(f"📡 Testing API at: {api_base}")
    print()
    
    # Test suite
    tests = [
        ("Health Check", test_health),
        ("Voice Listing", test_voices),
        ("Indonesian TTS", test_indonesian_tts),
        ("English TTS", test_english_tts),
        ("Batch TTS", test_batch_tts),
        ("Service Stats", test_stats)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"🧪 {test_name}")
        try:
            if test_func(api_base):
                passed += 1
            else:
                failed += 1
        except KeyboardInterrupt:
            print("\n⚠️ Test interrupted by user")
            break
        except Exception as e:
            print(f"❌ {test_name} crashed: {e}")
            failed += 1
        
        print()
        time.sleep(1)  # Brief pause between tests
    
    # Results
    print("=" * 50)
    print(f"📊 Test Results:")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {(passed/(passed+failed)*100):.1f}%" if (passed+failed) > 0 else "No tests run")
    
    if failed == 0:
        print("\n🎉 All tests passed! Your Edge-TTS API is working perfectly!")
        print(f"🌐 API accessible at: {api_base}")
        print(f"📖 Documentation: {api_base}/docs")
    else:
        print(f"\n⚠️ {failed} test(s) failed. Check your configuration.")
        print("💡 Tip: Make sure Docker services are running and ports are open")

if __name__ == "__main__":
    main()