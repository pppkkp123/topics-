from test_data import get_test_data
from congestion import calc_congestion_score, filter_ahead_events
from filters import is_false_congestion
from confidence import calc_report_confidence

def evaluate():
    data = get_test_data()

    correct = 0
    total = len(data)

    TP = 0
    FP = 0
    FN = 0

    print("=== 開始驗證 ===\n")

    for d in data:
        speed = d["speed"]
        events = d["events"]
        reports = d["reports"]

        # 車輛方向（假設）
        vehicle_heading = 0

        # 只取前方事件
        events = filter_ahead_events(events, vehicle_heading)

        # 計算回報可信度
        for r in reports:
            r.confidence = calc_report_confidence(r, len(reports))

        # 誤判排除
        is_false = is_false_congestion(
        speed_info=speed,
        stop_duration=d["stop_duration"],
        near_signal=d["near_signal"],
        events=events,
        reports=reports
        )

        if is_false:
            prediction = 0
            score = 0
        else:
            score = calc_congestion_score(speed, events, reports)
            prediction = 1 if score >= 0.35 else 0

        label = d["label"]

        print(f"{d['name']}")
        print(f"壅塞分數: {round(score,2)} 預測:{prediction} 真實:{label}")
        print("------")

        if prediction == label:
            correct += 1

        if prediction == 1 and label == 1:
            TP += 1
        elif prediction == 1 and label == 0:
            FP += 1
        elif prediction == 0 and label == 1:
            FN += 1

    accuracy = correct / total
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0

    print("\n=== 結果 ===")
    print(f"準確率 Accuracy: {round(accuracy,2)}")
    print(f"精確率 Precision: {round(precision,2)}")
    print(f"召回率 Recall: {round(recall,2)}")


if __name__ == "__main__":
    evaluate()
