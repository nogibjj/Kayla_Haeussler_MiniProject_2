from main import (
    get_summary_stats,
    create_histogram,
    create_scatter
)

import pandas as pd

def test_get_summary_stats():
    summary_stats= get_summary_stats(pd.read_csv("StudentPerformanceFactors.csv"), "Exam_Score")
    assert summary_stats["mean"] == 67.235659
    assert summary_stats["50%"] == 67
    assert summary_stats["std"] == 3.890456



def test_create_histogram():
    create_histogram(pd.read_csv("StudentPerformanceFactors.csv"), "Exam_Score") 

def test_create_scatter():
    create_scatter(pd.read_csv("StudentPerformanceFactors.csv"), "Hours_Studied", "Exam_Score")

test_get_summary_stats()
test_create_histogram()
test_create_scatter()