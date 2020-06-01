def parse_file(filepath):
    data = []
    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        while line:
            key, match = _parse_line(line)
            if key == 'country':
                country = match.group('country')
            if key == 'grade':
                grade = match.group('grade')
                grade = int(grade)
            if key == 'name_score':
                value_type = match.group('name_score')
                line = file_object.readline()
                while line.strip():
                    number, value = line.strip().split(',')
                    value = value.strip()
                    row = {
                        'country': country,
                        'Grade': grade,
                        'country_code': number,
                        value_type: value
                    }
                    data.append(row)
                    line = file_object.readline()
            line = file_object.readline()
        data = pd.DataFrame(data)
        data.set_index(['country', 'Grade', 'country_code'], inplace=True)
        data = data.groupby(level=data.index.names).first()
        data = data.apply(pd.to_numeric, errors='ignore')
    return data
