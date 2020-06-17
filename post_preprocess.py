test['selected_text'] = test.apply(lambda x: post_process(x['selected_text']) if (len(str(x['selected_text']).split())==1) else x['selected_text'], axis=1)
test['Jaccard'] = test.apply(lambda x: jaccard(str(x.selected_text), str(x.selected_text)), axis=1)
