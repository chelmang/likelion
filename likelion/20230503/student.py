from abc import *

class StudentManagerRepo:
    @abstractmethod
    def add_student(self, name,student_no, age, major, gpa): # 학생 추가
        pass

    @abstractmethod
    def list_student(self): # 전체 학생 조회
        pass

    @abstractmethod
    def search_student(self, name): # 학생 조회
        pass

    @abstractmethod
    def delete_student(self, name): # 학생 제거
        pass

    @abstractmethod
    def update_student(self, name, student): # 학생 수정
        pass
    
class StudentManageImpl(StudentManagerRepo):
    def __init__(self):
        super().__init__()
        self.__students = []
        
    def add_student(self, name):
        for student in self.__students:
            if student.get_name() == name:
                print(f"{name} 학생이 이미 존재합니다.")
                return
        student_no = input("학번: ")
        age = input("나이: ")
        major = input("전공: ")
        gpa = input("학점: ")
        student = Student(student_no, name, age, major, gpa)
        self.__students.append(student)
        print(f"{name} 학생이 추가되었습니다.")
        
    def delete_student(self, name):
        for student in self.__students:
            if student.get_name() == name:
                self.__students.remove(student)
                return
        raise ValueError(f"{name} 학생이 존재하지 않습니다.")
    
    def update_student(self, name, student):
        for s in self.__students:
            if s.get_name() == name:
                s.student_no = student.student_no
                s.age = student.age
                s.major = student.major
                s.gpa = student.gpa
                return
        raise ValueError(f"{name} 학생이 존재하지 않습니다.")

    def search_student(self, name):
        for student in self.__students:
            if student.get_name() == name:
                return student
        raise ValueError(f"{name} 학생이 존재하지 않습니다.")
    def list_student(self):
        return self.__students
    

class StudentManagerService:
    def __init__(self):
        self.__student_repo = StudentManageImpl()

    def add_student(self, student): # 학생 추가
        self.__student_repo.add_student(student)

    def list_student(self): # 전체 학생 조회
        return self.__student_repo.list_student()

    def search_student(self, name): # 학생 조회
        return self.__student_repo.search_student(name)

    def delete_student(self, name): # 학생 제거
        self.__student_repo.delete_student(name)

    def update_student(self, name, student): # 학생 수정
        self.__student_repo.update_student(name, student)
    
    def sort_gpa(self):
        students = self.__student_repo.list_student()
        return sorted(students, key=lambda student: student.get_gpa(), reverse=True) 

class Student:
    def __init__(self, student_no, name, age, major, gpa):
        self.student_no = student_no
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
    
    def __str__(self):
        return f"이름: {self.name}\n학번: {self.student_no}\n나이: {self.age}\n전공: {self.major}\n학점: {self.gpa}"

    def get_student_no(self):
        return self.student_no

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_major(self):
        return self.major

    def get_gpa(self):
        return self.gpa
    

def main(manager):

    
    while True:
        print("==============")
        print("1. 학생 추가")
        print("2. 전체 학생 조회")
        print("3. 학생 조회")
        print("4. 학생 제거")
        print("5. 학생 수정")
        print("6. 종료")
        print("==============")
        select = int(input(": "))
        
        if select == 1:        
                name = input("이름: ")
                result = manager.add_student(name)
                if result is None:
                    print(f"{name} 학생이 이미 존재합니다.")
                else:    
                    student_no = input("학번: ")
                    age = input("나이: ")
                    major = input("전공: ")
                    gpa = input("학점: ")
                
                    manager.student_info(name, student_no, age, major, gpa)
                    print(f"{name} 학생이 추가되었습니다.") 

        
        elif select == 2:
            students = manager.list_student()
            if students:
                for student in students:
                    print(student)
            else:
                print("학생이 존재하지 않습니다.")
                
        elif select == 3:
            name = input("이름: ")
            try:
                student = manager.search_student(name)
                print(student)
            except ValueError as e:
                print(e)
                
        elif select == 4:
            try:
                manager.delete_student(name)
                print(f"{name} 학생 제거가 완료되었습니다.")
            except ValueError as e:
                print(e)
        
        elif select == 5:
            name = input("이름: ")

            student = manager.add_student(name)
            if student:
                student_no = input("학번: ")
                age = input("나이: ")
                major = input("전공: ")
                gpa = input("학점: ")

                manager.update_student(student, student_no, age, major, gpa)
                print(f"{name} 학생 수정이 완료되었습니다.")
            else:
                print(f"{name} 학생이 존재하지 않습니다.")
        elif select == 6:
            break       

if __name__ == '__main__':
    manager = StudentManagerService()
    main(manager)