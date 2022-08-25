def menu():
    print('{:_^30}'.format(' CLASSROOM MENU '))
    print('CONSULT LIST', '{: >17}'.format('(1)'))
    print('ADD STUDENT', '{: >18}'.format('(2)'))
    print('SEARCH STUDENT', '{: >15}'.format('(3)'))
    print('REMOVE STUDENT', '{: >15}'.format('(4)'))


def show_list():
    print('{:_^30}'.format(' STUDENTS LIST '))
    for student in students:
        print(f'STUDENT: ')
        for k_data, v_data in student.items():
            print('{0}: {1: <16}'.format(k_data.upper(), v_data))
        print('{:_^30}'.format('_'))


def add_student():
    fullname = input('Enter the name of student (Name and Surname): ').title()
    fullname = fullname.split(" ")
    name, surname = fullname
    students.append({'id': len(students) + 1, 'name': name, 'surname': surname})


def search_student():
    search_control = False
    target_student = input('Enter the name of the student you want to find: ').title()
    print('SEARCHING...')
    for student in students:
        for k_data, v_data in student.items():
            if target_student == student['name']:
                search_control = True
                print('{0}: {1: <16}'.format(k_data.upper(), v_data))
    if not search_control:
        print('NOT FOUND')


def remove_student():
    control = True
    while control:
        target = input('Enter the ID of the student you want to remove: ')

        if not target.isalpha():
            target = int(target)
        else:
            print('ID IS A NUMBER')
            continue

        for i, student in enumerate(students):
            if student['id'] == target:
                print(f'THE STUDENT IS {student["name"]} {student["surname"]}')
                choice = input('ARE YOU SURE THAT YOU WANT TO REMOVE? y/n \n').lower()
                if not choice == 'y':
                    continue
                else:
                    del(students[i])
                    control = False


students = [
    {
        'id': 1,
        'name': 'Nic',
        'surname': 'Lima',
    },
    {
        'id': 2,
        'name': 'Francinny',
        'surname': 'Gomes',
    },
    {
        'id': 3,
        'name': 'Fernanda',
        'surname': 'Gomes',
    },
]


exit_q = True
while exit_q:
    menu()
    option = input('OPTION: ')
    if option == '1':
        show_list()
    elif option == '2':
        add_student()
    elif option == '3':
        search_student()
    elif option == '4':
        remove_student()
    else:
        print('Invalid option')

    exit_control = input('If you want to quit, type "q": ').lower()
    if exit_control == 'q':
        exit_q = False
