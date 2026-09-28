# Các bài toán chính của dự án

Ngày chốt: 27/9/2026. Tài liệu này tách dự án thành các bài toán chính, các module phục vụ chúng, và các nhánh quyết định gắn với mốc và hạn nộp. Nó dựa trên `direction.md`.

Nhãn người đề xuất dùng giống như trong `direction.md`. Nhãn *(phannhatminh đề xuất)* và nhãn *(huysuy05 đề xuất)* chỉ ý của từng thành viên. Nhãn *(Claude đề xuất, phannhatminh chốt)* chỉ những ý do Claude đưa ra trong lúc trao đổi, sau đó được phannhatminh chốt vào tài liệu.

## 1. Dự án có bốn bài toán chính

Việc tách dự án thành bốn bài toán dưới đây là *(Claude đề xuất, phannhatminh chốt)*.

**Bài toán thứ nhất: người nói truyền đạt gì khi dùng chữ "believe", và người nghe là người nhận được bao nhiêu?** *(phannhatminh đề xuất)* Bài toán này đo khoảng hở giao tiếp giữa người với người. Nó là bài toán chính vì hai lý do. Lý do thứ nhất là nó tự thành một phát hiện khoa học xã hội, đủ đứng riêng thành một bài. Lý do thứ hai là nó cung cấp mốc so cho mọi bài toán còn lại.

**Bài toán thứ hai: AI làm người nghe nhận được bao nhiêu so với người nghe là người?** *(phannhatminh đề xuất)* Đây là phép so hai khoảng cách với cùng một mốc là ý người nói. Nó là kết quả trung tâm của phần hành vi.

**Bài toán thứ ba: khi AI hiểu, mỗi cách hiểu được biểu diễn bên trong AI như thế nào?** *(phannhatminh đề xuất, note.md)* Đây là câu hỏi chính thứ nhất của phần cơ chế.

**Bài toán thứ tư: khi AI hiểu lệch, lỗi nằm ở biểu diễn hay ở bước đọc ra?** *(huysuy05 đề xuất)* Đây là câu hỏi chính thứ hai của phần cơ chế.

Bốn bài toán này gom thành hai tầng. Bài toán thứ nhất và thứ hai thuộc tầng hành vi. Bài toán thứ ba và thứ tư thuộc tầng cơ chế. Hai tầng này ứng đúng với mức 1 và mức 2–3 trong `note.md` §2.

Mỗi bài toán ở tầng sau cần kết quả của bài toán ở tầng trước:

- Bài toán thứ hai cần kết quả của bài toán thứ nhất, vì mốc so là ý người nói.
- Bài toán thứ ba cần bài toán thứ hai chỉ ra những tình huống mà AI hiểu đúng.
- Bài toán thứ tư cần bài toán thứ hai chỉ ra những tình huống mà AI hiểu lệch.

Việc sửa mô hình không phải bài toán chính. Nó là một ứng dụng kỹ thuật, và chỉ được làm nếu bài toán thứ hai cho thấy AI lệch nhiều hơn người. Khung lý thuyết, bộ tình huống, hệ thống chạy mô hình, kiểm tra bên ngoài và hạ tầng cơ chế cũng không phải bài toán chính. Chúng là điều kiện để giải bốn bài toán trên.

## 2. Mười một module phục vụ bốn bài toán

Cách chia module là *(Claude đề xuất, phannhatminh chốt)*. Nội dung của từng module lấy từ `direction.md`.

**Module 1 là khung lý thuyết.** Nó định nghĩa ba cách hiểu chữ "believe" và ba vai gồm người nói, người nghe là người và AI làm người nghe, đủ rõ để đo được. Đầu ra là tiêu chí vận hành cho từng cách hiểu và bản đăng ký trước. Module này phục vụ cả bốn bài toán. Nó không phụ thuộc module nào, nhưng có thể phải sửa lại sau Mốc 1.

**Module 2 là bộ tình huống.** Nó viết những đoạn văn thể hiện đúng từng cách hiểu mà không mắc yếu tố gây nhiễu. Bộ lõi có 96 tình huống, mỗi tình huống có tám phiên bản, và câu nói việc tin có ích được chia thành hai loại. Kèm theo là 24 tình huống về việc tin vào kết cục xấu để tự thúc đẩy. Mỗi tình huống cần một bản nêu sự thật không dùng chữ "believe" cho người nói, và một bản có câu đích cho người nghe. Module này phục vụ cả bốn bài toán và phụ thuộc Module 1.

**Module 3 là nghiên cứu người nói.** Nó đo mức tin chắc s và cách hiểu mà người nói muốn truyền đạt khi dùng câu đích. Module này phục vụ bài toán thứ nhất, và cung cấp mốc so cho bài toán thứ hai và thứ tư. Nó phụ thuộc Module 2 và giấy duyệt IRB.

**Module 4 là nghiên cứu người nghe là người.** Nó đo mức tin chắc h và cách hiểu mà người nghe nhận được. Module này phục vụ bài toán thứ nhất và thứ hai. Nó phụ thuộc Module 2 và giấy duyệt IRB.

**Module 5 là hệ thống chạy AI làm người nghe.** Nó thu mức tin chắc m và cách hiểu của nhiều mô hình qua ba dạng câu hỏi: câu hỏi có hoặc không, con số từ 0 đến 100, và câu hỏi phân loại tường minh. Module này phục vụ bài toán thứ hai. Nó phụ thuộc Module 2, nhưng phần hạ tầng có thể dựng trước trên pilot.

**Module 6 là phân tích khoảng cách.** Nó tính khoảng cách của người nghe và khoảng cách của AI so với ý người nói, rồi so hai khoảng cách theo từng tình huống. Nó cũng xử lý hai điểm công bằng: phân bố của từng người nghe riêng lẻ, và sự bất đồng giữa những người nói. Module này giải bài toán thứ nhất và thứ hai. Nó phụ thuộc Module 3, 4 và 5.

**Module 7 là kiểm tra bên ngoài.** Nó kiểm tra xem kết quả có tổng quát sang dữ liệu đã công bố của Vesga và của Cusimano không, kèm các bản diễn đạt lại để kiểm tra nhiễm dữ liệu. Module này phục vụ bài toán thứ hai. Nó chỉ phụ thuộc Module 5, nên làm được ngay.

**Module 8 là hạ tầng cơ chế và đối chứng dương.** Nó chạy mô hình ở độ chính xác đầy đủ với thư viện can thiệp, và xác nhận rằng quy trình tìm lại được cơ chế đã biết của Steele và cộng sự. Module này phục vụ bài toán thứ ba và thứ tư. Nó không phụ thuộc module nào, nên làm được ngay.

**Module 9 giải bài toán thứ ba.** Nó hỏi mỗi cách hiểu được biểu diễn thành một biến thống nhất hay thành các thành phần rời, và hỏi cách hiểu được hình thành tại từ "believes" hay chỉ khi mô hình bị hỏi. Module này phụ thuộc Module 8, Module 2, và Module 3 để có nhãn cách hiểu từ người nói.

**Module 10 giải bài toán thứ tư.** Nó hỏi khi AI hiểu lệch, lỗi nằm ở biểu diễn hay ở bước đọc ra. Module này phụ thuộc Module 8, Module 3 để có đích s, và Module 5.

**Module 11 là sửa mô hình.** Nó thu hẹp khoảng cách của AI bằng một can thiệp ReFT tại các vị trí đã định vị, rồi so với ba cách sửa khác *(huysuy05 đề xuất)*. Module này là phần có điều kiện, không phải bài toán chính. Nó phụ thuộc Module 6 để biết có khoảng cách rõ rệt hay không, và phụ thuộc Module 10 để biết chỗ đặt can thiệp.

Ngoài các module trên có một việc hành chính chạy xuyên suốt. Việc đó gồm hồ sơ IRB và việc công bố dữ liệu lên Hugging Face kèm siêu dữ liệu Croissant, vì nhánh Evaluations & Datasets của NeurIPS bắt buộc điều này.

## 3. Các nhánh quyết định gắn với mốc và hạn nộp

Hạn nộp năm 2027 chưa được công bố, nên mọi ngày tháng dưới đây lấy theo lịch năm 2026. Ba mốc quyết định là của Huy *(huysuy05 đề xuất)*. Hai nhánh về IRB và về CogSci là phần thêm vào *(Claude đề xuất, phannhatminh chốt)*.

**Ở Mốc 1, vào cuối tháng 10, dữ liệu thử của Module 3 và Module 4 quyết định Module 1 có đứng được không.**

- Nếu người nói muốn truyền đạt mức tin chắc thấp mà người nghe hiểu thành cao, thì có một khoảng hở thật trong giao tiếp, và Module 2 được viết tiếp ở quy mô đầy đủ.
- Nếu chính người nói cũng muốn truyền đạt mức tin chắc cao, thì Module 1 phải được sửa trước khi viết tiếp Module 2.
- Nếu những người nói bất đồng nhiều với nhau, thì các tình huống mơ hồ trong Module 2 phải được thiết kế lại.

**Giấy duyệt IRB là điểm nghẽn của toàn bộ lịch nộp.**

- Nếu IRB duyệt kịp để thu dữ liệu đầy đủ trong tháng 12 và tháng 1, thì lịch nộp tháng 5 vẫn giữ được.
- Nếu IRB duyệt chậm đến tháng 2 hoặc muộn hơn, thì Module 3, 4 và 6 sẽ không xong trước đầu tháng 5. Khi đó phần bộ đánh giá chuyển sang chu kỳ tháng 5 hoặc chu kỳ tháng 8 của ACL Rolling Review.

**Hạn nộp CogSci, vào khoảng đầu tháng 2, chỉ dành cho một bài thuần về người.**

- Nếu đến cuối tháng 1 Module 3 và Module 4 đã có dữ liệu đầy đủ, và khoảng hở giữa người nói với người nghe là một phát hiện rõ ràng, thì nhóm có thể gửi riêng phần này tới CogSci.
- Nếu dữ liệu chưa đủ, nhóm bỏ qua hạn này. Theo lịch của Huy, dữ liệu người đầy đủ chỉ xong vào khoảng tháng 1, nên khả năng kịp là thấp.

**Ở Mốc 2, vào giữa tháng 2, kết quả của Module 6 quyết định Module 11 có được làm không.**

- Nếu khoảng cách của AI lớn hơn rõ rệt so với khoảng cách của người nghe là người, thì nhóm làm Module 11 trong tháng 3.
- Nếu hai khoảng cách tương đương, hoặc AI lệch ít hơn người, thì nhóm bỏ Module 11. Khi đó bài báo cáo hai khoảng cách cùng kết quả của Module 9 và Module 10.

**Ở Mốc 3, vào giữa tháng 3, nhóm chọn nơi nộp theo những module đã xong.**

- Nếu Module 2 đến Module 7 đã xong và dữ liệu đã sẵn sàng để công bố, thì nhóm nộp nhánh Evaluations & Datasets của NeurIPS. Hạn năm 2026 là ngày 4/5 cho phần tóm tắt và ngày 6/5 cho bài đầy đủ.
- Nếu Module 9 hoặc Module 10 có kết quả trước đầu tháng 5, thì nhóm gửi thêm phần cơ chế tới workshop về diễn giải cơ chế tại ICML, với hạn năm 2026 là ngày 8/5. Workshop này không lưu trữ chính thức và nhận cả bài đang được NeurIPS phản biện, nên hai bài có thể nộp song song.
- Nếu bộ đánh giá không kịp ngày 6/5 nhưng kịp khoảng ba tuần sau, thì nhóm nộp chu kỳ tháng 5 của ACL Rolling Review cho EMNLP hoặc AACL, với hạn năm 2026 là ngày 25/5.
- Nếu phần cơ chế chưa có kết quả đến tháng 5, thì bài chính được nộp mà không có phần cơ chế. Phần cơ chế được viết thành một bài riêng cho chu kỳ sau.

**Module 9 có một nhánh quyết định riêng, không phụ thuộc lịch nộp.**

- Nếu bộ phân loại không tách được các cách hiểu tốt hơn mô hình túi từ, thì đó là một kết quả âm. Kết quả này vẫn báo cáo được, vì đối chứng dương của Module 8 cho thấy quy trình hoạt động đúng. Nhánh Evaluations & Datasets của NeurIPS nhận kết quả âm.
- Nếu các cách hiểu tách được ngay tại từ "believes", hoặc chỉ tách được ở vị trí cuối, thì kết quả nào cũng là một phát hiện về thời điểm AI hình thành cách hiểu.
