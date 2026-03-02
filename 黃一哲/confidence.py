import math

def calc_report_confidence(report, nearby_reports=1):
    """
    使用者回報可信度
    """

    # 距離越近越可信
    dist_score = max(0, 1 - report.distance / 500)

    # 越新越可信
    time_score = max(0, 1 - report.minutes_ago / 10)

    # 多人回報加強
    crowd_score = min(1, math.log(nearby_reports + 1) / 2)

    return 0.5*dist_score + 0.3*time_score + 0.2*crowd_score
