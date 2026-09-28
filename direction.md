# Hướng đi của dự án theo kế hoạch của Huy

Ngày chốt: 27/9/2026. Bản này dựa trên `revised_plan_believe.md` (commit 45a3d97), có thêm hai điều chỉnh rút ra từ phần kiểm chứng.

## 1. Câu hỏi nghiên cứu giữ nguyên, nhưng hình thức của bài thay đổi

Câu hỏi vẫn như cũ. Khi đọc câu "X believes that p", trong đó câu này giữ nguyên từng chữ và chỉ đoạn văn phía trước thay đổi, mô hình có hiểu niềm tin của X giống như người đọc hiểu không? Điểm khác là bài không còn coi câu hỏi này như một phép thử có sẵn đáp án đúng. Bài sẽ gồm hai phần:

- phần đầu là một bộ đánh giá chuẩn (benchmark), với đáp án tham chiếu lấy từ phán đoán của người đọc thật;
- phần sau phân tích cơ chế bên trong mô hình.

Lý do cho thay đổi này là ở những tình huống quan trọng nhất, chưa ai biết chắc câu trả lời đúng. Vì vậy phán đoán của người thật phải đóng vai trò đáp án. Mục tiêu là nộp bài vào khoảng tháng 5 năm 2027.

## 2. Khung lý thuyết có ba cách hiểu chữ "believe" thay vì hai

Kế hoạch giữ nguyên hai cách hiểu mà dự án đã có từ đầu:

- Theo cách hiểu thứ nhất, một người tin điều gì đó vì bằng chứng cho thấy điều đó đúng.
- Theo cách hiểu thứ hai, một người tin điều gì đó vì việc tin giúp họ có kết cục tốt hơn, dù họ biết khả năng điều đó xảy ra là thấp.

Kế hoạch của Huy thêm một cách hiểu thứ ba: một người tin điều gì đó vì họ mong nó xảy ra, và mong muốn đó khiến họ đánh giá khả năng xảy ra cao hơn mức bằng chứng cho phép. Cách hiểu thứ ba này thường được gọi là wishful thinking.

Trong tài liệu này, "mức tin chắc" là xác suất mà chính người tin tự đánh giá cho điều họ tin. Theo khung ba cách hiểu, kết quả của pilot có một cách diễn giải mới. Mô hình gán mức tin chắc cao cho người tin theo cách hiểu thứ hai, vậy là mô hình đã hiểu họ theo cách hiểu thứ ba.

Kế hoạch đặt ra bốn giả thuyết:

- Giả thuyết thứ nhất: mô hình gán cho người tin theo cách hiểu thứ hai một mức tin chắc cao hơn mức mà người đọc gán.
- Giả thuyết thứ hai: khi đoạn văn nói người tin đang sợ hãi hoặc đang hy vọng, người đọc và mô hình sẽ hiểu chữ "believe" khác nhau.
- Giả thuyết thứ ba: mô hình sẽ hiểu sai những tình huống mà người tin chủ động tin vào một kết cục xấu để tự thúc đẩy bản thân. Ví dụ là một sinh viên tin rằng mình sẽ trượt để tiếp tục ôn bài.
- Giả thuyết thứ tư hỏi vì sao mô hình sai. Khả năng thứ nhất là bên trong mô hình không có chỗ nào lưu riêng mức tin chắc của người tin. Khả năng thứ hai là mô hình có lưu thông tin đó nhưng không dùng đến khi trả lời.

## 3. Các tình huống thử nghiệm được viết lại để loại bỏ những yếu tố gây nhiễu mà pilot mắc phải

Mỗi tình huống sẽ có thêm một câu nói về cảm xúc của người tin và một câu nêu mức tin chắc mà chính người tin tự nói ra. Mỗi tình huống được viết thành tám phiên bản khác nhau. Phiên bản quan trọng nhất là phiên bản trong đó người tin tự nói rằng cơ hội của mình chỉ khoảng một phần mười. Đây là phép thử rõ ràng nhất cho giả thuyết thứ nhất, vì văn bản đã nêu thẳng mức tin chắc.

Câu nói rằng việc tin có ích được chia thành hai loại:

- Ở loại thứ nhất, việc tin cải thiện một kết cục khác với điều được tin. Ví dụ, bệnh nhân Maya tin ca mổ sẽ thành công, và việc tin giúp cô hồi phục tốt hơn sau mổ.
- Ở loại thứ hai, việc tin làm tăng khả năng xảy ra của chính điều được tin. Ví dụ, võ sĩ tin mình sẽ thắng thì đánh tốt hơn.

Với loại thứ hai, đoạn văn phải nêu thêm rằng ngay cả những người tin chắc cũng hiếm khi thành công. Nếu không, người đọc có lý do chính đáng để nâng mức tin chắc lên. Phần kiểm chứng cho thấy cách chia này là cần thiết. Trong pilot có ba tình huống thuộc loại thứ nhất, và ở hai trong số đó, mô hình Qwen2.5-7B gần như không nâng mức tin chắc. Điều này gợi ý rằng phần lớn kết quả mà pilot gọi là "gộp niềm tin với mức tin chắc" có thể đến từ yếu tố gây nhiễu, chứ chưa chắc là lỗi hiểu của mô hình.

Bộ tình huống chính dự kiến có 96 tình huống trên 8 lĩnh vực. Kèm theo đó là 24 tình huống về việc tin vào kết cục xấu để tự thúc đẩy. 24 tình huống của pilot sẽ được dùng làm bộ phát triển.

## 4. Mô hình được đo bằng nhiều cách hỏi, và các chỉ số chính đều tính bằng cách so sánh với người

Ba câu hỏi có hoặc không của pilot được giữ lại, và mỗi câu có thêm một cách diễn đạt thứ hai. Kế hoạch thêm ba cách đo:

- Cách thứ nhất yêu cầu mô hình đưa ra mức tin chắc dưới dạng một con số từ 0 đến 100.
- Cách thứ hai hỏi thẳng mô hình rằng người tin giữ niềm tin chủ yếu vì bằng chứng hay chủ yếu vì việc tin có ích.
- Cách thứ ba lấy từ nghiên cứu của Vesga và cộng sự. Nó đo xem mô hình ưu tiên viết "thinks" hay "believes", và ưu tiên viết "decided to believe" hay "decided whether to believe".

Có ba chỉ số chính:

- Chỉ số thứ nhất đo xem khi đoạn văn thêm câu nói việc tin có ích, mức tin chắc mà mô hình gán tăng lên nhiều hơn hay ít hơn mức mà người đọc gán.
- Chỉ số thứ hai đo khoảng cách giữa mức tin chắc mà mô hình gán và con số mà chính văn bản đã nêu.
- Chỉ số thứ ba đo mức độ câu trả lời của mô hình khớp với câu trả lời của người, so với mức các nhóm người khớp với nhau.

Kế hoạch chạy trên các mô hình mã nguồn mở thuộc hai đến ba họ khác nhau. Với mỗi họ, kế hoạch lấy cả bản gốc lẫn bản đã được huấn luyện để làm theo chỉ dẫn. Kế hoạch cũng chạy thêm vài mô hình thương mại qua API.

## 5. Phần thu thập phán đoán của người là phần nghiên cứu khoa học xã hội của bài

Kế hoạch cần khoảng 190 người tham gia qua nền tảng Prolific, với chi phí khoảng 760 đô la. Thiết kế nghiên cứu phải được đăng ký trước. Hội đồng đạo đức nghiên cứu (IRB) phải duyệt trước khi thu dữ liệu.

Kế hoạch dùng hai nghiên cứu đã công bố trên người làm bộ kiểm tra bên ngoài. Đó là nghiên cứu của Vesga và cộng sự năm 2025, và nghiên cứu của Cusimano và Lombrozo năm 2021. Mỗi tình huống gốc từ các nghiên cứu này sẽ được chạy song song với một bản diễn đạt lại. Lý do là mô hình có thể đã gặp bản gốc trong dữ liệu huấn luyện.

Bộ dữ liệu WishfulEval chỉ còn một vai trò: làm khuôn mẫu cho câu nói về cảm xúc. Đề xuất so sánh với chính niềm tin của mô hình bị bỏ. Đề xuất đó đo cách mô hình tự ước lượng xác suất, trong khi dự án đo cách mô hình hiểu niềm tin của người khác.

## 6. Phần phân tích cơ chế đi từ những phương pháp rẻ đến những phương pháp đắt

Phần này chạy trên hai mô hình Qwen2.5-7B và Llama-3.1-8B ở độ chính xác đầy đủ. Nó dùng bốn phương pháp theo thứ tự:

1. Phương pháp thứ nhất theo dõi câu trả lời hình thành dần qua từng tầng của mô hình.
2. Phương pháp thứ hai lấy trạng thái bên trong từ một đoạn văn và ghép vào đoạn văn kia. Làm vậy cho biết thông tin quyết định câu trả lời nằm ở tầng nào và ở từ nào.
3. Phương pháp thứ ba huấn luyện các bộ phân loại tuyến tính nhỏ. Mục đích là kiểm tra xem trạng thái bên trong có chứa mức tin chắc được nêu và có chứa việc đoạn văn có câu nói việc tin có ích hay không.
4. Phương pháp thứ tư tìm một không gian con nhỏ bên trong mô hình mang thông tin về mức tin chắc (phương pháp DAS). Sau đó nó kiểm tra xem thay đổi không gian con đó có làm câu trả lời thay đổi theo không.

Mục đích của cả bốn bước là trả lời giả thuyết thứ tư. Phần này có thể bắt đầu từ tháng 11 trên các tình huống của pilot, vì nó không cần dữ liệu người.

Nếu mô hình và người khác nhau rõ rệt, bước cuối cùng là sửa mô hình. Cách sửa là huấn luyện một can thiệp nhỏ đặt đúng tại các vị trí bên trong mô hình mà bước trước đã tìm ra (phương pháp ReFT). Cách sửa này sẽ được so với ba cách khác: đẩy trạng thái bên trong theo một hướng cố định, tinh chỉnh một phần nhỏ trọng số, và đơn giản là viết lại câu lệnh. Bất kỳ cách sửa nào cũng phải thỏa ba điều kiện:

- giữ nguyên mức tin chắc cao ở những tình huống người tin vì bằng chứng;
- không làm giảm kết quả trên bộ kiểm tra niềm tin sai BigToM;
- cải thiện ba chỉ số chính trên dữ liệu mà nó chưa từng thấy.

## 7. Có ba mốc quyết định có thể làm bài đổi hướng

- **Mốc thứ nhất, vào cuối tháng 10.** Nhóm thu phán đoán của 9 người bằng biểu mẫu hiện có. Có thể chính người đọc cũng cho rằng người tin theo cách hiểu thứ hai nghĩ điều họ tin có khả năng cao. Khi đó, cách đặt vấn đề "mô hình gộp niềm tin với mức tin chắc" phải bỏ. Bài sẽ chuyển thành phép thử xem mô hình có hiểu giống người hay không, và phần sửa mô hình có lẽ sẽ bị cắt.
- **Mốc thứ hai, vào giữa tháng 2.** Nhóm xem dữ liệu người đầy đủ có cho thấy mô hình khác người rõ rệt ở hai chỉ số đầu hay không. Nếu có, nhóm làm phần sửa mô hình. Nếu không, bài báo cáo mức độ mô hình khớp với người và giải thích cơ chế bên trong.
- **Mốc thứ ba, vào giữa tháng 3.** Nhóm chọn nơi nộp bài.

Nơi nộp ưu tiên là nhánh Evaluations & Datasets của hội nghị NeurIPS, hạn khoảng đầu tháng 5. Phần phân tích cơ chế được gửi thêm tới workshop về diễn giải cơ chế tại hội nghị ICML. Phương án dự phòng là chu kỳ tháng 5 của ACL Rolling Review.

## 8. Trong hai tuần tới có sáu việc cụ thể cần làm

1. Thu phán đoán của 9 người bằng biểu mẫu hiện có.
2. Nộp hồ sơ lên hội đồng đạo đức nghiên cứu.
3. Tải các tình huống của Vesga và của Cusimano từ kho OSF, rồi chạy hai mô hình của pilot trên các tình huống đó.
4. Viết lại tệp `pilot/stimuli.py` theo tám phiên bản và hai loại câu nói việc tin có ích.
5. Chạy lại pilot trên Qwen2.5-7B ở độ chính xác đầy đủ và làm lượt ghép trạng thái bên trong đầu tiên.
6. Cập nhật `README.md` và `note.md` theo phạm vi mới.

Kế hoạch gợi ý chia công việc thành hai nhánh chạy song song. Một người phụ trách bộ đánh giá và phần nghiên cứu trên người, người kia phụ trách phần phân tích cơ chế.
