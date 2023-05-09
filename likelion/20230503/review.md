# 학생 관리 프로그램
##### reviewer: 염동환
1. Impl에서, add메소드가 인자로 이름만 입력받고 리스트에 해당 이름이 이미 존재하면 오류처리,<\br>
   이후 문제가 없다면 나머지 정보를 입력받아 student객체를 생성하고 students에 append하는게 참신했습니다.<\br>
   다만, main에서 select==1일 때 코드를 보면 중복회원을 걸러내는 작업은 동작하나, 중복회원이 아닌경우에 manager.student_info를 호출하는 것 같습니다.<\br>
   그리고 service클래스에 student_info라는 메소드가 없습니다.
    
2.  raise ValueError(f"{name} 학생이 존재하지 않습니다.")로 예외처리를 한 부분이 좋다고 생각합니다.

3.  Student클래스의 각 속성을 private으로 지정하지 않았는데, 속성 명 앞에 __를 붙여서 private 지정을 해야할 듯 합니다.

4.  Impl의 add_student에서 학생의 존재, 추가 여부를 출력 해주기에, main에서 result로 값을 받지 않고 또한 if문도 없애도 될 것 같습니다.

