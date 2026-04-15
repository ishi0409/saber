from bs4 import BeautifulSoup

def remove_html_tags(df):
    return BeautifulSoup(str(df), "html.parser").get_text()


def prepare_data(df):
    df['名前'] = df['名前'].apply(remove_html_tags)
    df_modify = df[["試合","打数", "四球", "塁打", "安打", "名前", "守備位置"]]
    return df_modify.groupby(["名前", "守備位置"], as_index=False).sum()
    

def RC(grouped_df):
    molecule = (grouped_df["安打"] + grouped_df["四球"]) * grouped_df["塁打"]
    denominator = (grouped_df["打数"] + grouped_df["四球"])
    return (molecule / denominator).fillna(0)

def total(df):
    new_df = prepare_data(df)
    new_df["RC"] = RC(new_df)
    res_series = new_df["RC"]
    return new_df[["名前", "守備位置", "RC"]].to_dict(orient='records')




    