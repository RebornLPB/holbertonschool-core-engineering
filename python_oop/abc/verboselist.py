#!/usr/bin/env python3

"""Module verboselist
Class verboselist that extends the python list class"""

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

if __name__ == "__main__":
    v_list = VerboseList()

    v_list.append("Smaug")

    v_list.extend(["Toothless", "Shenron"])

    v_list.remove("Smaug")

    popped_item = v_list.pop()

    v_list.append("Charizard")

    v_list.pop(0)
