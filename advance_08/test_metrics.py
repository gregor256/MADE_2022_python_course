import time
import stat_metrics


def test_stat_metrics() -> None:
    with stat_metrics.Stats.timer("calc"):  # 0.1
        time.sleep(1)
        res = stat_metrics.calc(3)  # 3

    stat_metrics.Stats.count("calc").add()
    stat_metrics.Stats.avg("calc").add(res)

    start_time = 0.0
    res = stat_metrics.calc(7)  # 7
    end_time = 3.0
    stat_metrics.Stats.timer("calc").add(end_time - start_time)  # 0.3
    stat_metrics.Stats.count("calc").add()
    stat_metrics.Stats.avg("calc").add(res)

    stat_metrics.Stats.count("http_get_data").add()
    stat_metrics.Stats.avg("http_get_data").add(0.7)

    stat_metrics.Stats.count("no_used")  # не попадет в результат collect

    collected_metrics = stat_metrics.Stats.collect()

    collected_metrics["calc.timer"] = round(collected_metrics["calc.timer"], 2)
    assert set(collected_metrics.keys()) == {"calc.count", "calc.avg", "calc.timer",
                                             "http_get_data.count", "http_get_data.avg"}
    assert collected_metrics["calc.count"] == 2
    assert collected_metrics["calc.avg"] == 5
    assert 3.5 <= collected_metrics["calc.timer"] <= 4.5
    assert collected_metrics["http_get_data.count"] == 1
    assert collected_metrics["http_get_data.avg"] == 0.7

    collected_metrics = stat_metrics.Stats.collect()

    assert not collected_metrics
