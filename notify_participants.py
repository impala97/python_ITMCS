"""
A solution to notify the participants in the quiz competition.
This code is compatible with python2.7 & python3.6 as well.
python notify_participants.py
"""

__author__ = 'Smit R. Mehta'
__author_email__ = 'mehtasmit44@gmail.com'
__date_time__ = "10th Nov'20 19:00:00"


def notify_participant(data):
    """
    A Parent function that takes list as argument and process the data.
    Will return the name of participants that are..
    1. participated each days.
    2. participated only once.
    3. participated on the first day only.
    :param data:
    :return:
    """
    nos_of_day = len(data)  # Total number of days of competition.
    participant_data = dict()

    def _clean_data():
        """
        This function process the input data and forms a clean data to process it further.
        :return:
        """
        count_day = 1
        for competition_day in data:
            for participant in competition_day:
                if participant not in participant_data:
                    participant_data[participant] = {
                        'participated_day': 1,
                        'first_day': True if count_day == 1 else False
                    }
                else:
                    participant_data[participant]['participated_day'] += 1
                    participant_data[participant]['first_day'] = False
            count_day = count_day + 1  # Count to competition day.

    def _every_day_participant(cleaned_data):
        """
        A Logic to get the participants name who participated on every day.
        Based on the number of days participated in the quiz competition.
        :param cleaned_data:
        :return:
        """
        _participants_name = list()

        for participant in cleaned_data:
            if cleaned_data[participant]['participated_day'] == nos_of_day:
                _participants_name.append(participant)

        _participants_name.sort()  # Alphabetically sorted.
        return _participants_name

    def _participated_only_once(cleaned_data):
        """
        A Logic to get the participants name who participated only once.
        Based on the number of days participated in the quiz competition.
        :param cleaned_data:
        :return:
        """
        _participants_name = list()

        for participant in cleaned_data:
            if cleaned_data[participant]['participated_day'] == 1:
                _participants_name.append(participant)

        _participants_name.sort()  # Alphabetically sorted.
        return _participants_name

    def _participated_on_first_day(cleaned_data):
        """
        A Logic to get the participants name who participated on the first day only.
        Based on the flag in the cleaned_data dict.
        :param cleaned_data:
        :return:
        """
        _participants_name = list()

        for participant in cleaned_data:
            if cleaned_data[participant]['first_day']:
                _participants_name.append(participant)

        _participants_name.sort()  # Alphabetically sorted.
        return _participants_name

    _clean_data()
    # print(participant_data)
    participated_daily = _every_day_participant(participant_data)
    participated_only_once = _participated_only_once(participant_data)
    participated_on_first_day = _participated_on_first_day(participant_data)

    return participated_daily, participated_only_once, participated_on_first_day


if __name__ == '__main__':
    p1, p2, p3 = notify_participant([
        ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole'],
        ['Brad', 'Walter', 'Sam', 'Krish', 'Desmond', 'Jennifer'],
        ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
        ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
        ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
        ['Krish', 'Brad', 'Walter', 'Jennifer', 'Desmond', 'Harry', 'Nicole', 'Sam']
    ])

    print("Participants Names who participated daily :: {}".format(p1))
    print("Participants Names who participated only once :: {}".format(p2))
    print("Participants Names who participated on first day :: {}".format(p3))
