# Phương pháp luận cho bài toán thứ nhất

Ngày viết: 27/9/2026. Trạng thái: **đề xuất, chưa chốt.**

Bài toán thứ nhất hỏi: người nói truyền đạt gì khi dùng chữ "believe", và người nghe là người nhận được bao nhiêu? Bài toán này được định nghĩa trong `problems.md` mục 1.

Toàn bộ phương pháp luận trong tệp này là *(Claude đề xuất)*, trừ những chỗ ghi rõ nguồn khác. Những ý đã có trong các tài liệu khác được ghi kèm tên tệp. Khi phannhatminh chốt một ý, nhãn của ý đó sẽ được đổi thành *(Claude đề xuất, phannhatminh chốt)*.

## 1. Khung chung là một thí nghiệm giao tiếp giữa hai nhóm người có thông tin bất cân xứng

Dạng thí nghiệm này quen thuộc trong tâm lý ngôn ngữ học, dưới tên thí nghiệm sản sinh và thông hiểu. Người nói biết trạng thái bên trong của nhân vật, gồm mức tin chắc của nhân vật và lý do nhân vật giữ niềm tin. Người nghe chỉ thấy đoạn văn và câu đích. Khoảng hở giao tiếp là phần thông tin mà người nói muốn truyền đi nhưng không đến được người nghe.

## 2. Người nói và người nghe nhìn thấy cùng một đoạn văn

Người nói đọc đúng đoạn văn mà người nghe sẽ đọc. Điểm khác duy nhất là người nói được biết thêm các sự thật riêng tư về nhân vật. Ví dụ, người nói đọc đoạn văn về Maya, và được biết thêm rằng Maya tự đánh giá cơ hội thành công khoảng một phần mười và chọn giữ thái độ tin tưởng vì thái độ đó giúp cô hồi phục tốt hơn.

Việc các sự thật riêng tư phải được viết bằng ngôn ngữ không chứa chữ "believe" đã có trong `direction.md` mục 3 *(phannhatminh đề xuất)*. Điểm mới ở đây là người nói đọc cùng đoạn văn với người nghe. `direction.md` chưa nói rõ điểm này.

Thiết kế này có hai lợi ích. Lợi ích thứ nhất là mọi khác biệt giữa hai nhóm chỉ đến từ thông tin riêng tư, không đến từ việc hai nhóm đọc hai văn bản khác nhau. Lợi ích thứ hai là câu đích được giữ nguyên từng chữ, đúng như đề bài yêu cầu.

Có một cách làm khác là cho người nói tự viết mô tả, rồi đưa mô tả đó cho người nghe đọc. Cách này tự nhiên hơn, nhưng nó phá điều kiện câu đích giữ nguyên. Vì vậy cách này chỉ được dùng như một phần mở rộng nhỏ ở mục 8, không dùng làm thiết kế chính.

## 3. Người nói trả lời ba câu hỏi

Ba câu hỏi đã có trong `direction.md` mục 3. Tệp này chỉ làm rõ vai trò và cách diễn đạt của từng câu.

1. **Câu hỏi thứ nhất hỏi người nói có chấp nhận dùng câu đích để mô tả nhân vật hay không.** Câu hỏi này đóng vai bộ lọc. Chỉ những tình huống mà đa số người nói chấp nhận câu đích mới được coi là một cách dùng chữ "believe" hợp lệ. Ngưỡng "đa số" phải được đăng ký trước.
2. **Câu hỏi thứ hai hỏi người nói muốn người đọc hiểu rằng nhân vật tự đánh giá cơ hội là bao nhiêu, trên thang từ 0 đến 100.** Câu hỏi phải hỏi về điều người nói muốn truyền đạt, không hỏi về mức tin chắc thật của nhân vật. Mức tin chắc thật đã được cho sẵn, nên nếu hỏi về nó thì câu trả lời chỉ lặp lại con số được cho. Con số trả lời cho câu hỏi này là s.
3. **Câu hỏi thứ ba hỏi người nói muốn người đọc hiểu rằng nhân vật tin chủ yếu vì lý do nào.** Có ba lựa chọn: vì bằng chứng, vì việc tin có ích, hoặc vì mong muốn điều đó xảy ra. Ba lựa chọn này ứng với ba cách hiểu trong `direction.md` mục 2.

## 4. Người nghe trả lời hai câu hỏi tương ứng trên cùng thang đo

1. **Câu hỏi thứ nhất hỏi người nghe nghĩ nhân vật tự đánh giá cơ hội là bao nhiêu, trên thang từ 0 đến 100.** Con số trả lời cho câu hỏi này là h. Việc dùng thang 0 đến 100 cho bên nghe đã có trong `direction.md` mục 5 *(huysuy05 đề xuất)*.
2. **Câu hỏi thứ hai hỏi người nghe nghĩ nhân vật tin chủ yếu vì lý do nào, với cùng ba lựa chọn như câu hỏi của người nói.** Câu hỏi phân loại tường minh này có trong kế hoạch của Huy *(huysuy05 đề xuất)*. Việc đặt nó song song với câu hỏi của người nói là phần thêm vào.

Biểu mẫu hiện có trong `pilot/human_form.template.html` dùng thang 1 đến 7 cho ba câu hỏi của pilot (`note.md` §9.2). Biểu mẫu này cần được sửa sang thang 0 đến 100 để so trực tiếp được với câu trả lời của người nói.

## 5. Phép phân tích chính là một mô hình hỗn hợp với tương tác giữa vai và điều kiện

Việc dùng mô hình hỗn hợp với hiệu ứng ngẫu nhiên cho người tham gia và cho tình huống có trong kế hoạch của Huy *(huysuy05 đề xuất)*. Kế hoạch đó chỉ áp dụng cho người nghe. Điểm mới ở đây là thêm biến vai.

Mô hình được đặc tả như sau:

- Biến phụ thuộc là mức tin chắc được trả lời, trên thang 0 đến 100.
- Biến cố định thứ nhất là vai, gồm người nói và người nghe.
- Biến cố định thứ hai là cách hiểu mà tình huống hướng tới.
- Mô hình có hiệu ứng ngẫu nhiên cho người tham gia và cho tình huống.

Kết quả cần tìm nằm ở tương tác giữa vai và cách hiểu. Ở những tình huống người tin vì bằng chứng, người nói và người nghe được kỳ vọng cho con số gần nhau, nên các tình huống này là đối chứng tự nhiên. Nếu khoảng hở chỉ xuất hiện, hoặc lớn hơn hẳn, ở những tình huống người tin vì việc tin có ích, thì chữ "believe" gây mất thông tin đúng ở cách hiểu thứ hai. Đó là phát hiện của bài toán thứ nhất.

Câu hỏi về lý do của niềm tin được phân tích theo cùng logic. Đại lượng được đo là tỉ lệ người nghe chọn đúng lý do mà đa số người nói muốn truyền đạt, và tỉ lệ này được so giữa các cách hiểu.

Khoảng cách có dấu h trừ s, cùng phép kiểm định theo cặp trên từng tình huống, đã có trong `direction.md` mục 3. Hai điểm công bằng trong `direction.md` mục 3 vẫn áp dụng ở đây. Điểm thứ nhất là s phải được xử lý như một phân bố, vì người nói có thể bất đồng. Điểm thứ hai là cần báo cáo phân bố của từng người nghe, không chỉ báo cáo trung bình.

## 6. Thiết kế cần sáu biện pháp kiểm soát

1. **Người nói và người nghe là hai nhóm người tách biệt.** Không ai được tham gia cả hai vai. Điểm này đã có trong `direction.md` mục 6.
2. **Dùng Latin square để mỗi người chỉ thấy mỗi tình huống ở đúng một phiên bản.** Latin square đã có trong biểu mẫu hiện có và trong kế hoạch của Huy.
3. **Có câu kiểm tra thông hiểu cho người nói.** Ví dụ, người nói phải trả lời lại con số mà nhân vật tự đánh giá. Câu này bảo đảm người nói đã nắm các sự thật riêng tư trước khi trả lời.
4. **Có câu kiểm tra chú ý cho cả hai nhóm.** Biểu mẫu hiện có đã có câu kiểm tra chú ý.
5. **Cỡ mẫu được tính bằng phân tích lực thống kê, dựa trên dữ liệu thử của Mốc 1.** Hồ sơ IRB và ngân sách cần con số này, và hiện nó chưa có.
6. **Giả thuyết, tiêu chí loại người tham gia và phép phân tích chính được đăng ký trước khi thu dữ liệu đầy đủ.** Yêu cầu đăng ký trước đã có trong `note.md` §3 và trong kế hoạch của Huy.

## 7. Thiết kế có ba mối đe dọa đến tính hợp lệ, và bài phải nêu rõ chúng

1. **Người nói trong thí nghiệm là người nói đóng vai.** Họ không tự nhiên muốn mô tả Maya, mà chỉ được giao các sự thật rồi được hỏi. Vì vậy ý định của họ có thể khác ý định của người nói ngoài đời.
2. **Câu hỏi chấp nhận có thể gợi ý câu trả lời.** Việc hỏi người nói có chấp nhận câu đích hay không có thể khiến họ chấp nhận nhiều hơn so với khi họ tự chọn từ. Phần mở rộng ở mục 8 giúp đo mức độ của vấn đề này.
3. **Người tham gia trên Prolific chủ yếu là người nói tiếng Anh ở Mỹ.** Vì vậy khoảng hở đo được có thể không tổng quát sang các cộng đồng ngôn ngữ khác.

## 8. Phần mở rộng cho người nói tự viết mô tả

Trong phần mở rộng, một nhóm nhỏ người nói được biết các sự thật về nhân vật và tự viết một câu mô tả niềm tin của nhân vật. Nhóm nghiên cứu đếm tần suất người nói chọn "believes", "thinks" hay "hopes".

Phần này dùng lại thước đo của Vesga và cộng sự ở phía người nói. `direction.md` mục 5 đã quyết định rằng thước đo đó chỉ dùng cho người nói là người, nhưng chưa nói cách dùng. Phần mở rộng này là cách dùng cụ thể.

Phần mở rộng cũng trả lời một câu hỏi nền cho toàn bộ bài toán: trong đời thực, người nói có tự chọn chữ "believe" cho cách hiểu thứ hai hay không. Nếu người nói hiếm khi tự chọn chữ đó, thì bài toán thứ nhất cần được đặt lại.

## 9. Còn một điểm mở cần quyết định trước khi chốt

Thiết kế 8 danh sách Latin square và yêu cầu ít nhất 5 đánh giá cho mỗi ô trong kế hoạch của Huy được tính cho riêng người nghe. Công thức trần nhiễu của Huy cũng vậy. Khi có thêm nhóm người nói, cần quyết định hai điều. Điều thứ nhất là người nói có dùng cùng 8 danh sách với người nghe hay không. Điều thứ hai là mỗi ô tình huống nhân phiên bản cần bao nhiêu người nói.
