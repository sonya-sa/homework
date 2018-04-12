
inventory_log = {"Day 1":'um-deliveries-20140519.txt', "Day 2":'um-deliveries-20140520.txt', "Day 3":'um-deliveries-20140521.txt'}


def delivery_report(dict):
    for day in inventory_log:
        the_file = open(inventory_log[day])
        print day
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]

            print "Delivered {} {}s for total of ${}".format(
                count, melon, amount)
        the_file.close()

delivery_report(inventory_log)
