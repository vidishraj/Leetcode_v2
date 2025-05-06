from collections import defaultdict

class Solution(object):
    def invalidTransactions(self, transactions):
        """ 
        - Record all transactions done at a particular time. Recording the person and the location. Example:
            `['alice,20,800,mtv','bob,50,1200,mtv','bob,20,100,beijing']` :\n
            ` 
            {   
            20: {'alice': {'mtv'}, 'bob': {'beijing'}}, 
            50: {'bob': {'mtv'}}
            } 
            ` \n
            `{time: {person: {location}, person2: {location1, location2}}, time: {person: {location}}}`
        - For each transaction, check if the amount is invalid - and add it to the invalid transactions if so.
        - For each transaction, go through invalid times (+-60), check if a transaction by the same person happened
            in a different city - and add it to the invalid transactions if so.
        """
        invalid = []

        # Record all transactions done at a particular time
        #   including the person and the location.
        transaction_time = defaultdict(dict)
        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            if name not in transaction_time[time]:
                transaction_time[time][name] = {city, }
            else:
                transaction_time[time][name].add(city)

        for transaction in transactions:
            name, str_time, amount, city = transaction.split(",")
            time = int(str_time)

            # # check amount
            if int(amount) > 1000:
                invalid.append(transaction)
                continue

            # # check if person did transaction within 60 minutes in a different city
            for inv_time in range(time-60, time+61):
                if inv_time not in transaction_time:
                    continue
                if name not in transaction_time[inv_time]:
                    continue

                trans_by_name_at_time = transaction_time[inv_time][name]

                # check if transactions were done in a different city
                if city not in trans_by_name_at_time or len(trans_by_name_at_time) > 1:
                    invalid.append(transaction)
                    break

        return invalid