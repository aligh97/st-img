import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

def run():
    st.sidebar.info('Welcome Reyhaneh Mokhtari')

    data = pd.read_json('data/mokhtari.json')

    def date_range(start, end):
        delta = end - start  # as timedelta
        days = [start + timedelta(days=i) for i in range(delta.days + 1)]
        return days

    start_date = st.date_input('from date:')
    end_date = st.date_input('to date:')
    dates = date_range(start_date, end_date)


    text = st.selectbox('select option', ['annotated images',
                                          'skipped images',
                                          'total objects'
                                          ])

    num_skip = 0
    num_labels = 0
    num_img = 0

    skip, labels, total_img = [], [], []

    for date in dates:
        # number_img_annotated = len(data)
        for i in range(len(data)):
            created_at = data['annotations'][i][0]['created_at'][:10]
            if str(created_at) == str(date):
                num_img += 1
                if data['annotations'][i][0]['was_cancelled'] == False: 
                    for j in range(len(data['annotations'][i][0]['result'])):
                        if data['annotations'][i][0]['result'][j]['from_name'] == "label":
                            num_labels+=1
                else:
                    num_skip += 1
                    # number_img_annotated -= 1
        
        # num_img += number_img_annotated

        # output = ''

    if text == 'annotated images':
        st.success(num_img - num_skip)
    elif text == 'skipped images':
        st.success(num_skip)
    elif text == 'total objects':
        st.success(num_labels)

if __name__ == "__main__":
    run()
