'''
@app.route('/titanic/train', methods=['GET'])
def train():
    # using random forest as an example
    # can do the training separately and just update the pickles
    df = pd.read_csv(training_data)
    df_ = df[include]
    categoricals = []  # going to one-hot encode categorical variables
    for col, col_type in df_.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            df_[col].fillna(0, inplace=True)  # fill NA's with 0 for ints/floats, too generic

    # get_dummies effectively creates one-hot encoded variables
    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)
    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]
    # capture a list of columns that will be used for prediction
    global model_columns
    model_columns = list(x.columns)
    joblib.dump(model_columns, model_columns_file_name)
    global clf
    clf = rf()
    start = time.time()
    clf.fit(x, y)
    print('Trained in %.1f seconds' % (time.time() - start))
    print('Model training score: %s' % clf.score(x, y))
    joblib.dump(clf, model_file_name)
    return 'Success'

@app.route('/titanic/wipe', methods=['GET'])
def wipe():
    try:
        shutil.rmtree('model')
        os.makedirs(model_directory)
        return 'Model wiped'
    except Exception as e:
        print(str(e))
        return 'Could not remove and recreate the model directory'
'''