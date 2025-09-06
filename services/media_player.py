# services/media_player.py
from datetime import datetime, timedelta, timezone
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
from winrt.windows.foundation import TimeSpan, DateTime

playback_status_map = {
    0: "Closed",
    1: "Opened",
    2: "Changing",
    3: "Stopped",
    4: "Playing",
    5: "Paused"
}

def convert_datetime_offset(windows_datetime: DateTime):
    windows_epoch = datetime(1601, 1, 1, tzinfo=timezone.utc)
    microseconds = windows_datetime.universal_time // 10
    return windows_epoch + timedelta(microseconds=microseconds)

async def get_current_media_info():
    manager = await MediaManager.request_async()
    session = manager.get_current_session()
    if not session:
        return {"error": "Media not found."}

    info = await session.try_get_media_properties_async()
    timeline = session.get_timeline_properties()
    playback_info = session.get_playback_info()

    base_position = timeline.position
    updated_time = convert_datetime_offset(timeline.last_updated_time)
    now = datetime.now(timezone.utc)

    position_seconds = base_position.duration // 10_000_000
    if playback_info.playback_status == 4:  # Playing
        elapsed = (now - updated_time).total_seconds()
        position_seconds += int(elapsed)

    duration_seconds = timeline.end_time.duration // 10_000_000

    pos = f"{position_seconds // 3600:02}:{(position_seconds % 3600) // 60:02}:{position_seconds % 60:02}"
    dur = f"{duration_seconds // 3600:02}:{(duration_seconds % 3600) // 60:02}:{duration_seconds % 60:02}"
    status_text = playback_status_map.get(playback_info.playback_status, f"Unknown({playback_info.playback_status})")

    return {
        "title": info.title,
        "artist": info.artist,
        "status": status_text,
        "position": pos,
        "duration": dur
    }

async def control_media(command: str):
    manager = await MediaManager.request_async()
    session = manager.get_current_session()
    if not session:
        return {"error": "Media not found."}

    command = command.lower()
    if command == "play":
        await session.try_play_async()
    elif command == "pause":
        await session.try_pause_async()
    elif command == "next":
        await session.try_skip_next_async()
    elif command == "previous":
        await session.try_skip_previous_async()
    else:
        return {"error": f"'{command}' command undefined."}

    return {"status": f"'{command}' sent."}
