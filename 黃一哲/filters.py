def is_false_congestion(speed_info, stop_duration, near_signal, events, reports):
    """
    排除紅燈或短暫停車
    """

    # 🚦 紅燈停等（低速 + 在路口 + 短時間）
    if speed_info.current_speed < 10:
        if stop_duration < 60 and near_signal:
            return True

    # 🚗 短暫停車（但沒有事件、沒有回報才排除）
    if stop_duration < 20:
        if len(events) == 0 and len(reports) == 0:
            return True

    return False
