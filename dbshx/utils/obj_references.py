
def check_just_one_not_none(*value_refname):
    nones=0
    for a_tuple in value_refname:
        if a_tuple[0] is not None:
            nones += 1
    if nones != 1:
        raise ValueError(error_message_for_non_compatible_references([a_tuple[1] for a_tuple in value_refname]))


def error_message_for_non_compatible_references(list_of_ref_names):
    return "You must provide one and only one of the following params: " + str(list_of_ref_names)

