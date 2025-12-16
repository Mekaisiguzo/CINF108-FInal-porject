
import sys 

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        #Show help menu if no arguments were passed.
        print("todo cli")
        print("commands:")
        print("list [--list-name file]")
        print("add category \"description\" [--list-name file]")
        print("status id status [--list-name file]")
        print("update id")
        print("--category category")
        print("--description \"text\"")
        print("--status status")
        print("--list-name file")
        return

    list_name = "todo.txt"

    if "--list-name" in args:
        #see if the person using the program gave a special name for the list file
        i = args.index("--list-name")
        if i + 1 >= len(args):
            print("error has occurred: --list-name needs a filename")
            return
        list_name = args[i + 1]
        args.pop(i)
        args.pop(i)

    if len(args) == 0:
        print("error has occurred: missing command")
        return

    command = args[0]

    # for list
    if command == "list":
         #shows all tasks in the todo file
        try:
            f = open(list_name, "r")
            lines = f.readlines()
            f.close()
        except:
            print("no tasks found")
            return

        if len(lines) == 0:
            print("no tasks found")
            return

        for line in lines:
            print(line.strip())
        return

    #for add
    elif command == "add":
        if len(args) < 3:
            print("error has occurred: add needs category and description")
            return
        #adds a new task to the todo file that needs to be done

        category = args[1]
        description = args[2]
        status = "incomplete"

        try:
            f = open(list_name, "r")
            lines = f.readlines()
            f.close()
        except:
            lines = []

        task_id = len(lines) + 1

        #the format for task category, descriptions,status, ect
        new_task = str(task_id) + "|" + category + "|" + description + "|" + status

        f = open(list_name, "a")
        f.write(new_task + "\n")
        f.close()

        print("task added with id", task_id)
        return

    #forstatus

    elif command == "status":
        if len(args) < 3:
            print("error has occurred: status needs id and status")
            return

        try:
            task_id = int(args[1])
        except:
            print("error has occurred: id must be a number")
            return

        new_status = args[2]
       #for changimg the status on task thats been made



        #print error statments if status value is wrong
        if new_status != "incomplete" and new_status != "in progress" and new_status != "complete":
            print("error has occurred: status must be incomplete, in progress, or complete")
            return

        try:
            f = open(list_name, "r")
            lines = f.readlines()
            f.close()
        except:
            print("no tasks found")
            return

        f = open(list_name, "w")
        found = False

        for line in lines:
            parts = line.strip().split("|")
            if int(parts[0]) == task_id:
                parts[3] = new_status
                found = True
            f.write(parts[0] + "|" + parts[1] + "|" + parts[2] + "|" + parts[3] + "\n")

        f.close()

        if found:
            print("status updated")
        else:
            print("task not found")
        return

    # for update
    elif command == "update":
        if len(args) < 2:
            print("error has occurred: update needs id")
            return

        try:
            task_id = int(args[1])
        except:
            print("error has occurred: id must be a number")
            return

        new_category = None
        new_description = None
        new_status = None
    #helps updates the state, description, category




#looks at the update settings
        i = 2
        while i < len(args):
            if args[i] == "--category":
                if i + 1 >= len(args):
                    print("error has occurred: --category needs a value")
                    return
                new_category = args[i + 1]
                i += 2

            elif args[i] == "--description":
                if i + 1 >= len(args):
                    print("error has occurred: --description needs a value")
                    return
                new_description = args[i + 1]
                i += 2

            elif args[i] == "--status":
                if i + 1 >= len(args):
                    print("error has occurred: --status needs a value")
                    return
                new_status = args[i + 1]
                i += 2

            else:
                print("error has occurred: unknown option", args[i])
                return
            
            # if not atleast one update was given, the user will recive an an error has occure 
        if new_category is None and new_description is None and new_status is None:
            print("error has occurred: no updates given")
            return

        if new_status is not None:
            if new_status != "incomplete" and new_status != "in progress" and new_status != "complete":
                print("error has occurred: status must be incomplete, in progress, or complete")
                return

        try:
            f = open(list_name, "r")
            lines = f.readlines()
            f.close()
        except:
            print("no tasks found")
            return

        # rewrites file with new task values
        f = open(list_name, "w")
        found = False

        for line in lines:
            parts = line.strip().split("|")
            if int(parts[0]) == task_id:
                if new_category is not None:
                    parts[1] = new_category
                if new_description is not None:
                    parts[2] = new_description
                if new_status is not None:
                    parts[3] = new_status
                found = True
            f.write(parts[0] + "|" + parts[1] + "|" + parts[2] + "|" + parts[3] + "\n")

        f.close()

        if found:
            print("task updated")
        else:
            print("task not found")
        return

    else:
        print("error has occurred: unknown command")
        return


if __name__ == "__main__":
    main()
