from altair.datasets import data
import plotly.express as px
import pandas as pd

# update/add code below ...


def load_titanic():
    df = pd.read_csv("https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv")
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def survival_demographics():
    df = load_titanic()
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 12, 19, 59, float("inf")],
        labels=["Child", "Teen", "Adult", "Senior"],
    )
    grouped = df.groupby(
        ["pclass", "sex", "age_group"],
        observed=False
    )
    results = grouped.agg(
        n_passengers=("survived", "size"),
        n_survivors=("survived", "sum"),
        survival_rate=("survived", "mean"),
    ).reset_index()
    return results


def visualize_demographic():
    data = survival_demographics()
    fig = px.bar(
        data,
        x="age_group",
        y="survival_rate",
        color="sex",
        facet_col="pclass",
        barmode="group",
        labels={
            "age_group": "Age Group",
            "survival_rate": "Survival Rate",
            "sex": "Sex",
            "pclass": "Passenger Class",
        },
        title="Titanic Survival Rate by Age Group, Sex, and Passenger Class",
    )
    return fig


def family_groups():
    df = load_titanic()
    df["family_size"] = (
        df["sibsp"] + df["parch"] + 1
    )
    grouped = df.groupby(
        ["family_size", "pclass"],
        observed=False
    )
    results = grouped.agg(
        n_passengers=("fare", "size"),
        avg_fare=("fare", "mean"),
        min_fare=("fare", "min"),
        max_fare=("fare", "max"),
    ).reset_index()
    results = results.sort_values(
        ["family_size", "pclass"]
    )
    return results


def visualize_families():
    data = family_groups()
    data["pclass"] = "Class " + data["pclass"].astype(str)    
    fig = px.bar(
        data,
        x="family_size",
        y="avg_fare",
        color="pclass",
        barmode="group",
        labels={
            "family_size": "Family Size",
            "avg_fare": "Average Fare",
            "pclass": "Passenger Class",
        },
        title="Average Fare by Family Size and Passenger Class",
    )
    return fig


def last_names():
    df = load_titanic()
    last_names = df["name"].str.split(",").str[0]
    return last_names.value_counts()
    
