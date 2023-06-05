# Đối tượng đỉnh
class Vertex:
    # Khởi tạo với 3 thuộc tính: giá trị của đỉnh, danh sách các đỉnh kề và
    # danh sách giá trị các đỉnh kề
    def __init__(self, value):
        self.value = value
        self.neighbors_value = []
        self.neighbors_vertex = []

    # Thêm đỉnh kề (hàm này sẽ dùng để tạo cạnh)
    def add_neighbor(self, vertex):
        # Kiểm tra các đỉnh đã nằm kề với nó, nếu như tìm thấy thì báo là đã liên kết
        for i in self.neighbors_value:
            if vertex.value == i:
                print("Phần tử", vertex.value, "đã liên kết với", self.value)
                return
        # Thêm giá trị vào danh sách giá trị các đỉnh kề (chỉ 1 đỉnh vì có hướng)
        self.neighbors_value.append(vertex.value)
        # Thêm đỉnh vào danh sách các đỉnh kề (chỉ 1 đỉnh vì có hướng)
        self.neighbors_vertex.append(vertex)


# Đối tượng đồ thị có hướng
class DirectedGraph:
    # Khởi tạo với thuộc tính là một dictionary các đỉnh có dạng
    # [đỉnh]: [các đỉnh kề]
    def __init__(self):
        self.vertices = {}

    # Hàm tạo đỉnh mới
    def add_vertex(self, value):
        # Kiểm tra nếu đỉnh đã tồn tại
        for i in self.vertices:
            if i.value == value:
                print("Đỉnh đã tồn tại")
                return
        # Tạo một đối tượng đỉnh mới
        new_vertex = Vertex(value)
        # Thêm vào dictionary vertices
        self.vertices[new_vertex] = new_vertex.neighbors_vertex

    # Hàm thêm cạnh
    def add_edge(self, first_value, second_value):
        # Kiểm tra nếu một trong hai giá trị không tồn tại
        first_vertex = None
        second_vertex = None
        for i in self.vertices:
            if i.value == first_value:
                first_vertex = i
            if i.value == second_value:
                second_vertex = i
        if (first_vertex is None) or (second_vertex is None):
            print("Ít nhất 1 đỉnh không tồn tại")
            return
        # Dùng hàm thêm các đỉnh kề nói trên và cập nhật dictionary
        first_vertex.add_neighbor(second_vertex)
        self.vertices[first_vertex] = first_vertex.neighbors_vertex

    # In ra danh sách các đỉnh với các đỉnh kề của nó
    def adjacency_list(self):
        for i in self.vertices:
            print(i.value, "->", i.neighbors_value)

    # Duyệt theo chiều rộng
    def breadth_first_search(self, start_value):
        # Kiểm tra nếu đỉnh xuất phát tồn tại
        start_vertex = None
        for i in self.vertices:
            if i.value == start_value:
                 start_vertex = i
        if start_vertex is None:
            print("Đỉnh không tìm thấy")
            return
        # Copy dictionary các đỉnh và cho giá trị nằm sau đều là False
        # Ta sẽ thay đổi giá trị này khi đỉnh đã được thăm
        visited = self.vertices.copy()
        for i in visited:
            visited[i] = False
        # Tạo queue để duyệt theo chiều rộng
        queue = []
        # Thêm đỉnh xuất phát
        queue.append(start_vertex)
        # Và cho đỉnh xuất phát là đã thăm
        visited[start_vertex] = True
        # Duyệt cho đến khi queue trống thì kết thúc
        while queue:
            # Gán u là đỉnh đầu tiên trong queue
            u = queue.pop(0)
            # In giá trị u ra
            print(u.value, end=" ")
            # Thêm các đỉnh kề vào queue nếu như nó chưa thăm
            for i in u.neighbors_vertex:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    # Duyệt theo chiều sâu
    def depth_first_search(self, start_value):
        # Kiểm tra nếu đỉnh xuất phát tồn tại
        start_vertex = None
        for i in self.vertices:
            if i.value == start_value:
                start_vertex = i
        if start_vertex is None:
            print("Đỉnh không tìm thấy")
            return
        # Copy dictionary các đỉnh và cho giá trị nằm sau đều là False
        # Ta sẽ thay đổi giá trị này khi đỉnh đã được thăm
        visited = self.vertices.copy()
        for i in visited:
            visited[i] = False
        # Tạo stack để duyệt theo chiều sâu
        stack = []
        # Thêm đỉnh xuất phát
        stack.append(start_vertex)
        # Và cho đỉnh xuất phát là đã thăm
        visited[start_vertex] = True
        # Duyệt cho đến khi stack trống thì kết thúc
        while stack:
            # Gán u là đỉnh nằm trên cùng stack
            u = stack.pop()
            print(u.value, end=" ")
            # Thêm các đỉnh kề vào stack nếu như nó chưa thăm
            for i in u.neighbors_vertex:
                if visited[i] is False:
                    stack.append(i)
                    visited[i] = True


if __name__ == "__main__":
    graph = DirectedGraph()
    finish = False
    # Tạo vòng lặp vĩnh cửu, chương trình chỉ kết thúc khi finish = True
    while finish is not True:
        print()
        # Đoạn mã nhập lệnh bằng số đơn giản
        print("HELP: 1 - Thêm đỉnh, 2 - Thêm cạnh, 3 - In đồ thị, 4 - Duyệt đồ thị, 5 - Kết thúc")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if select == 1:
            value = input("Nhập giá trị của đỉnh: ")
            graph.add_vertex(value)
            continue
        elif select == 2:
            first_value = input("Nhập giá trị của đỉnh thứ nhất: ")
            second_value = input("Nhập giá trị của đỉnh thứ hai: ")
            graph.add_edge(first_value, second_value)
            continue
        elif select == 3:
            graph.adjacency_list()
            continue
        elif select == 4:
            start_value = input("Chọn vị trí bắt đầu: ")
            choice = abs(int(input("Chọn cách duyệt: 1 - Chiều rộng, 2 - Chiều sâu: ")))
            if choice == 1:
                graph.breadth_first_search(start_value)
            elif choice == 2:
                graph.depth_first_search(start_value)
            else:
                print("Số không hợp lệ!")
            continue
        elif select == 5:
            finish = True
            print("Chương trình kết thúc...")
        else:
            print("Số không hợp lệ!")
