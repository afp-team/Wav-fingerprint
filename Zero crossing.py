zero_crossing_rate_counter = 0  # licznik przejsc przez zero
        for i in range(0, len(fragment_data) - 1):
            if fragment_data[i] * -1 > 0 and fragment_data[i + 1] > 0:
                zero_crossing_rate_counter += 1
        zero_crossing_rate = zero_crossing_rate_counter / len(fragment_data)