def _finaldata(no_list,*args, **kwargs):
    final_list = []
    for stuff in no_list:
        new_stuff = stuff + 1
        final_list.append(new_stuff)
        return final_list
        
