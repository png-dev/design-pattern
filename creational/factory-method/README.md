Mục đích là khởi tạo một đối tượng mà không cần thiết cần chỉ ra khởi tạo từ một đối tượng nào cụ thể.

Cụ thể:
    - Tạo ra một factory method cho việc tạo đối tượng
    - Các lớp con kế thừa và có thể override lại method đó để chỉ rõ đối tượng mình khởi tạo
    
Được dùng khi.
    - Bạn chưa biết nên khởi tạo đối tượng từ class nào.
    - Muốn tập trung các đoạn code liên quan đến khởi tạo đối tượng về một nơi, đễ dễ thao tác và xử lý
    - Không muốn người dùng phải biết hết tên class liên quan đến khởi tạo đối tượng.
    