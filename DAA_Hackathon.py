class Job:
    def __init__(person, name, urgency, imp, est_time):
        person.name = name
        person.urgency = urgency
        person.imp = imp
        person.est_time = est_time

    def __str__(person):
        return f"{person.name} ({person.urgency}, {person.imp}, {person.est_time})"

class Optimizer:
    def __init__(person):
        person.jobs = []
    def add_job(person, job):
        person.jobs.append(job)
    def prioritize_jobs(person):
        person.jobs.sort(key=lambda job: (job.urgency, job.imp, job.est_time))
    def print_jobs(person):
        for job in person.jobs:
            print(job)

def main():
    todo_list = Optimizer()

    # Input for Jobs/Tasks
    while True:
        job_name = input("Enter Task name: ")
        job_urgency = input("Enter Urgency of the Task entered (l, m, h): ")
        job_imp = input("Enter the importance of the Task (l, m, h): ")
        job_est_time = input("Enter the estimated time to complete the Task (in minutes): ")

        #  To Create a new Task object and add it to the to-do list optimizer
        job = Job(job_name, job_urgency, job_imp, job_est_time)
        todo_list.add_job(job)

        more_jobs = input("Do you want to add more jobs (y/n)? ")
        if more_jobs.lower() != "y":
            break;
            
    print("Optimized Task List:")
    todo_list.prioritize_jobs()       # Prioritize the jobs
    todo_list.print_jobs()      # Print the jobs

if __name__ == "__main__":
    main()