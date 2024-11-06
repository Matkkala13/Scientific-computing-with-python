def arithmetic_arranger(problems = [], show_answers=False):
    number_of_problems = 0
    for number in problems:
        number_of_problems += 1
        if number_of_problems <= 5:
            pass
        else:
            return 'Error: Too many problems.'

    for problem in problems:
        for char in problem:
            if char == "*":
                return "Error: Operator must be '+' or '-'."
            elif char == "/":
                return "Error: Operator must be '+' or '-'."
            elif char.isalpha():
                return "Error: Numbers must only contain digits."
            else:
                pass
    
    translated_operations = []
    operation_translation = str.maketrans({" ":""})

    for problem in problems:
        translated_problem = problem.translate(operation_translation)
        translated_operations.append(translated_problem)

    final_format = []
    for operation in translated_operations:
        result = ''
        operation_translation2 = str.maketrans({"+":" ", "-":" "})
        translated_problem2 = operation.translate(operation_translation2)

        blank_index = translated_problem2.find(" ")
        second_index = blank_index + 1
        first_number = int(translated_problem2[0:blank_index])
        second_number = int(translated_problem2[second_index:100])
        first_number_string = translated_problem2[0:blank_index]
        second_number_string = translated_problem2[second_index:100]

        if len(first_number_string) > 4:
            return "Error: Numbers cannot be more than four digits."
        if len(second_number_string) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        for char in operation:
            if char == "+":
                result = first_number + second_number
                sign = "+"
            elif char == "-":
                result = first_number - second_number
                sign = "-"
            else:
                pass

        dashes = "-"*2 + "-"*max(len(first_number_string), len(second_number_string))

        if len(first_number_string) > len(second_number_string):
            space1 = " "*4 + " "*(len(dashes) - (max(len(first_number_string),len(second_number_string))))
            space2 = " " + " "*(len(first_number_string) - len(second_number_string))
        elif len(second_number_string) > len(first_number_string):
            space1 = " "*4 + " "*(len(dashes) - min(len(first_number_string),len(second_number_string)))
            space2 = " "
        else:
            space1 = " "*4 + " "*2
            space2 = " "

        space3 = " "*4 + " "*(len(dashes) - len(str(result)))
        final_format.append(first_number_string)
        final_format.append(sign)
        final_format.append(second_number_string)
        final_format.append(str(result))
        final_format.append(dashes)
        final_format.append(space1)
        final_format.append(space2)
        final_format.append(space3)

#format  
    def combiListenator(x, y, problem_counter):
        iteration = 0
        iterable = []
        number = [1, 2, 3, 4, 5]
        for num in number:
            iteration += 1
            iterable.append(iteration)
            if iteration == problem_counter:
                break

        combined_list = []
        for item in iterable:
            index = item - 1
            combined_list.append(x[index])
            combined_list.append(y[index])

        return combined_list

    def combiListenator2(x, y, z, problem_counter):
        iteration = 0
        iterable = []
        number = [1, 2, 3, 4, 5]
        for num in number:
            iteration += 1
            iterable.append(iteration)
            if iteration == problem_counter:
                break

        combined_list = []
        for item in iterable:
            index = item - 1
            combined_list.append(x[index])
            combined_list.append(y[index])
            combined_list.append(z[index])
            combined_list.append("    ")

        return combined_list

    first_numbers_finale = final_format[::8]    
    space1_finale = final_format[5::8]
    first_string = combiListenator(space1_finale, first_numbers_finale, number_of_problems)
    string1 = " "*(len(space1_finale[0]) - len("    ")) + "".join(first_string).strip(" ")

    sign_finale = final_format[1::8]
    space2_finale = final_format[6::8]
    second_numbers_finale = final_format[2::8]
    second_string = combiListenator2(sign_finale, space2_finale, second_numbers_finale, number_of_problems)
    second_string.pop(-1)
    string2 = "".join(second_string) 
    

    dashes_finale = final_format[4::8]
    string3 = "    ".join(dashes_finale)

    
    space3_finale = final_format[7::8]
    result_finale = final_format[3::8]
    third_string = combiListenator(space3_finale, result_finale, number_of_problems)
    
    
    if show_answers == True:
        string4 = " "*(len(space3_finale[0]) - len("    ")) + "".join(third_string).strip(" ")
        problem = f'{string1}\n{string2}\n{string3}\n{string4}'
    else:
        problem = f'{string1}\n{string2}\n{string3}'

    return problem
    

    