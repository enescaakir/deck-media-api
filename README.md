# 🎵 Deck Media API

**Deck Media API** is a powerful media control API developed for Windows systems. It provides comprehensive media player control and real-time monitoring using FastAPI and WebSocket technologies.

## 🌟 Features

- **🎵 Universal Media Control**: Control Spotify, Windows Media Player, YouTube, VLC, and all Windows media players
- **🚀 REST API Integration**: Simple HTTP endpoints for media control and information retrieval
- **🔄 Real-time WebSocket**: Live media status updates and notifications
- **⏯️ Complete Media Control**: Play, pause, skip next/previous track commands
- **📊 Rich Media Information**: Track details, artist info, playback position, and duration
- **⚡ High Performance**: Lightweight with minimal system resource usage

## 🏗️ Technology Stack

- **Backend**: FastAPI
- **WebSocket**: Native WebSocket support
- **Media Control**: Windows Media Transport Controls API
- **Runtime**: Windows Runtime (WinRT)
- **Time Management**: Native datetime handling

## 📋 Requirements

- **Operating System**: Windows 10/11
- **Python**: 3.8+
- **Windows Runtime**: WinRT support

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/enescaakir/deck-media-api.git
cd deck-media-api
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn winrt
```

### 4. Start the Application
```bash
python main.py
```

## 🌐 API Endpoints

The API runs on `http://localhost:3728`.

### 🎵 Media Information
```http
GET /media              # Get current media information
```

### 🎮 Media Control
```http
GET /media?action=play     # Start playback
GET /media?action=pause    # Pause playback
GET /media?action=next     # Skip to next track
GET /media?action=previous # Skip to previous track
```

## 📡 WebSocket Connection

Real-time media status monitoring:

- **Media Updates**: `ws://localhost:3728/ws/media`

### WebSocket Example
```javascript
const mediaSocket = new WebSocket('ws://localhost:3728/ws/media');
mediaSocket.onmessage = (event) => {
    const mediaInfo = JSON.parse(event.data);
    console.log('Now playing:', mediaInfo.title, '-', mediaInfo.artist);
};
```

## 📁 Project Structure

```
deck-media-api/
├── main.py                 # Main FastAPI application
├── services/
│   └── media_player.py    # Media control logic
└── README.md              # Documentation
```

## 🎯 Supported Media Players

This API works with any application supporting Windows Global System Media Transport Controls:

- **🎵 Spotify** - Full control support
- **🎬 Windows Media Player** - Complete integration
- **🌐 YouTube** - Browser-based control
- **🎵 Apple Music/iTunes** - Full compatibility
- **🎵 VLC Media Player** - Advanced control
- **🎵 Groove Music** - Native Windows support
- **🎵 Deezer** - Streaming service control
- **🎵 Tidal** - High-quality audio control

## 📊 API Response Format

### Media Information Response
```json
{
  "title": "Song Title",
  "artist": "Artist Name",
  "status": "Playing",
  "position": "02:15:30",
  "duration": "03:45:20"
}
```

### Control Command Response
```json
{
  "status": "'pause' sent."
}
```

### Error Response
```json
{
  "error": "Media not found."
}
```

## 🔧 Status Codes

| Code | Status | Description |
|------|--------|-------------|
| **0** | Closed | Media session closed |
| **1** | Opened | Media session opened |
| **2** | Changing | Status changing |
| **3** | Stopped | Playback stopped |
| **4** | Playing | Currently playing |
| **5** | Paused | Playback paused |

## 💡 Usage Examples

### Python Integration
```python
import requests

# Get current media info
response = requests.get('http://localhost:3728/media')
media = response.json()
print(f"♪ {media['title']} by {media['artist']}")

# Control playback
requests.get('http://localhost:3728/media?action=pause')
```

### JavaScript Integration
```javascript
// Real-time media monitoring
const ws = new WebSocket('ws://localhost:3728/ws/media');

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    if (!data.error) {
        updateUI(data.title, data.artist, data.status);
    }
};

// Media control
async function controlMedia(action) {
    await fetch(`http://localhost:3728/media?action=${action}`);
}
```

## 🐛 Troubleshooting

### Common Issues

**"Media not found" Error**
- Ensure a media player is running and playing content
- Check Windows media control permissions

**WebSocket Connection Failed**
- Verify port 3728 is not blocked by firewall
- Confirm the application is running with proper host configuration

**Import Errors**
- Install Windows Runtime: `pip install winrt`
- Ensure you're running on Windows 10/11

## 🤝 Contributing

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 📞 Contact

**Developer**: Enes Çakır  
[**Website**](https://enescakr.com/) | [**GitHub**](https://github.com/enescaakir) | [**LinkedIn**](https://www.linkedin.com/in/enescaakir/)

---

⭐ Don't forget to star this project if you like it!
