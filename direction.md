# Hướng đi của dự án theo kế hoạch của Huy

Ngày chốt: 27/9/2026. Bản này dựa trên `revised_plan_believe.md` (commit 45a3d97). Nó có thêm hai điều chỉnh rút ra từ phần kiểm chứng, và thêm thiết kế ba bên gồm người nói, người nghe là người và AI (mục 3).

Mỗi ý được gắn nhãn theo người đề xuất. Nhãn *(phannhatminh đề xuất)* và nhãn *(huysuy05 đề xuất)* chỉ ý của từng thành viên. Nhãn *(Claude đề xuất, phannhatminh chốt)* chỉ những ý do Claude đưa ra trong lúc kiểm chứng và trao đổi, sau đó được phannhatminh chốt vào tài liệu.

## 1. Câu hỏi nghiên cứu giữ nguyên, nhưng hình thức của bài thay đổi

Câu hỏi gốc vẫn như cũ *(phannhatminh đề xuất)*. Khi một câu "X believes that p" giữ nguyên từng chữ và chỉ đoạn văn phía trước thay đổi, chữ "believe" được hiểu theo cách nào?

Bài đặt câu hỏi này thành một câu hỏi về giao tiếp *(phannhatminh đề xuất)*. Người nói dùng chữ "believe" với một ý định cụ thể. Ý định đó đến được người nghe là người nhiều đến đâu, và đến được AI nhiều đến đâu khi AI làm việc nghe và hiểu?

Bài gồm hai phần *(huysuy05 đề xuất)*:

- phần đầu là một bộ đánh giá chuẩn (benchmark), có dữ liệu từ người nói thật và người nghe thật;
- phần sau phân tích cơ chế bên trong mô hình.

Mục tiêu là nộp bài vào khoảng tháng 5 năm 2027.

## 2. Khung lý thuyết có ba cách hiểu chữ "believe" thay vì hai

Kế hoạch giữ nguyên hai cách hiểu mà dự án đã có từ đầu *(phannhatminh đề xuất)*:

- Theo cách hiểu thứ nhất, một người tin điều gì đó vì bằng chứng cho thấy điều đó đúng.
- Theo cách hiểu thứ hai, một người tin điều gì đó vì việc tin giúp họ có kết cục tốt hơn, dù họ biết khả năng điều đó xảy ra là thấp.

Kế hoạch của Huy thêm một cách hiểu thứ ba: một người tin điều gì đó vì họ mong nó xảy ra, và mong muốn đó khiến họ đánh giá khả năng xảy ra cao hơn mức bằng chứng cho phép. Cách hiểu thứ ba này thường được gọi là wishful thinking *(huysuy05 đề xuất)*.

Trong tài liệu này, "mức tin chắc" là xác suất mà chính người tin tự đánh giá cho điều họ tin. Theo khung ba cách hiểu, kết quả của pilot có một cách diễn giải mới. Mô hình gán mức tin chắc cao cho người tin theo cách hiểu thứ hai, vậy là mô hình đã hiểu họ theo cách hiểu thứ ba *(huysuy05 đề xuất)*.

Kế hoạch đặt ra bốn giả thuyết *(huysuy05 đề xuất)*. Giả thuyết thứ nhất được viết lại theo hai khoảng cách ở mục 3 *(phannhatminh đề xuất)*.

- Giả thuyết thứ nhất: AI gán cho người tin theo cách hiểu thứ hai một mức tin chắc cao hơn mức mà người nói muốn truyền đạt, và độ lệch này lớn hơn độ lệch của người nghe là người.
- Giả thuyết thứ hai: khi đoạn văn nói người tin đang sợ hãi hoặc đang hy vọng, người nghe là người và AI sẽ hiểu chữ "believe" khác nhau.
- Giả thuyết thứ ba: AI sẽ hiểu sai những tình huống mà người tin chủ động tin vào một kết cục xấu để tự thúc đẩy bản thân. Ví dụ là một sinh viên tin rằng mình sẽ trượt để tiếp tục ôn bài.
- Giả thuyết thứ tư hỏi vì sao AI hiểu sai. Khả năng thứ nhất là bên trong mô hình không có chỗ nào lưu riêng mức tin chắc của người tin. Khả năng thứ hai là mô hình có lưu thông tin đó nhưng không dùng đến khi trả lời.

## 3. Thiết kế có ba bên: người nói, người nghe là người, và AI làm vai người nghe

Mỗi câu "X believes that p" liên quan đến ba vai. Vai thứ nhất là người tin, ví dụ Maya. Vai thứ hai là người nói, tức người dùng câu đó để mô tả Maya. Vai thứ ba là người nghe, tức người đọc câu đó và tự hiểu Maya tin gì. Người nói và người nghe có thể hiểu cùng một câu theo hai cách khác nhau. Trong dự án này, AI luôn làm vai người nghe *(phannhatminh đề xuất)*.

**Cách hiểu của người nói được thu từ người thật, không lấy từ nhóm nghiên cứu.** Trước đây, ý người nói chính là nhãn mà nhóm nghiên cứu gán khi viết đoạn văn. Giờ một nhóm người tham gia riêng sẽ đóng vai người nói *(phannhatminh đề xuất)*. Người nói được biết đầy đủ sự thật về nhân vật, và sự thật đó được viết bằng ngôn ngữ không chứa chữ "believe". Ví dụ, họ được biết rằng Maya tự đánh giá cơ hội thành công khoảng một phần mười, và Maya chọn giữ thái độ tin tưởng vì thái độ đó giúp cô hồi phục tốt hơn. Sau đó người nói trả lời ba câu hỏi *(Claude đề xuất, phannhatminh chốt)*:

1. Câu thứ nhất hỏi họ có chấp nhận mô tả Maya bằng câu đích, ví dụ "Maya believes that the surgery will succeed", hay không.
2. Câu thứ hai hỏi khi dùng câu đó, họ muốn người nghe hiểu Maya tin chắc đến đâu.
3. Câu thứ ba hỏi họ muốn người nghe hiểu Maya tin vì bằng chứng hay vì việc tin có ích.

Nhờ quy trình này, câu đích vẫn giữ nguyên từng chữ, đúng như đề bài yêu cầu.

**Người nghe là người và AI nhận cùng một đầu vào.** Cả hai đọc đoạn văn kèm câu đích và trả lời cùng các câu hỏi ở mục 5. Như vậy mỗi tình huống có ba con số về mức tin chắc: con số người nói muốn truyền đạt, con số người nghe là người hiểu được, và con số AI hiểu được.

**Phép so chính là so hai khoảng cách với cùng một mốc là ý người nói.** *(phannhatminh đề xuất)* Với mỗi tình huống, gọi s là mức tin chắc mà người nói muốn truyền đạt, h là mức tin chắc mà người nghe là người hiểu được, và m là mức tin chắc mà AI hiểu được. Khoảng cách của người nghe là h trừ s. Khoảng cách của AI là m trừ s. Hiệu giữa hai khoảng cách được tính trên từng tình huống rồi kiểm định theo cặp *(Claude đề xuất, phannhatminh chốt)*. Bài giữ cả dấu của khoảng cách, không chỉ lấy độ lớn. Dấu cho biết bên nghe hiểu mức tin chắc cao hơn hay thấp hơn ý người nói, nên chính dấu này kiểm tra giả thuyết thứ nhất.

**Cách so này bỏ được giả định rằng người nghe là người luôn đúng.** *(Claude đề xuất, phannhatminh chốt)* Trong thiết kế cũ, AI chỉ có thể khớp với người nghe hoặc kém hơn người nghe. Khi mốc so là ý người nói, AI có thể kém hơn người nghe, ngang bằng người nghe, hoặc hiểu đúng ý người nói hơn cả người nghe. Thiết kế cũ không thể phát hiện kết quả thứ ba.

**Có hai điểm phải thiết kế cẩn thận để phép so công bằng.** *(Claude đề xuất, phannhatminh chốt)*

- Điểm thứ nhất là người nghe là người gồm nhiều cá nhân, còn AI chỉ cho một câu trả lời. Nếu lấy trung bình của nhiều người nghe, nhiễu cá nhân bị triệt tiêu và phép so sẽ nghiêng về phía người. Vì vậy bài xếp khoảng cách của AI vào phân bố khoảng cách của từng người nghe riêng lẻ. Ví dụ, bài có thể báo cáo rằng AI hiểu lệch nhiều hơn tám mươi phần trăm số người nghe.
- Điểm thứ hai là người nói cũng không nhất trí với nhau. Cùng một bộ sự thật về Maya, người nói này có thể muốn truyền đạt mức tin chắc thấp, còn người nói khác lại muốn truyền đạt mức tin chắc cao hơn. Vì vậy s được xử lý như một phân bố chứ không phải một con số. Ở những tình huống mà người nói bất đồng nhiều, bản thân tình huống đã mơ hồ, nên khoảng cách của cả hai bên nghe ở đó phải được đọc thận trọng.

## 4. Các tình huống thử nghiệm được viết lại để loại bỏ những yếu tố gây nhiễu mà pilot mắc phải

Toàn bộ thiết kế tình huống trong mục này là của Huy *(huysuy05 đề xuất)*, trừ đoạn nêu kết quả kiểm chứng. Mỗi tình huống sẽ có thêm một câu nói về cảm xúc của người tin và một câu nêu mức tin chắc mà chính người tin tự nói ra. Mỗi tình huống được viết thành tám phiên bản khác nhau. Phiên bản quan trọng nhất là phiên bản trong đó người tin tự nói rằng cơ hội của mình chỉ khoảng một phần mười. Đây là phép thử rõ ràng nhất cho giả thuyết thứ nhất, vì văn bản đã nêu thẳng mức tin chắc.

Câu nói rằng việc tin có ích được chia thành hai loại:

- Ở loại thứ nhất, việc tin cải thiện một kết cục khác với điều được tin. Ví dụ, bệnh nhân Maya tin ca mổ sẽ thành công, và việc tin giúp cô hồi phục tốt hơn sau mổ.
- Ở loại thứ hai, việc tin làm tăng khả năng xảy ra của chính điều được tin. Ví dụ, võ sĩ tin mình sẽ thắng thì đánh tốt hơn.

Với loại thứ hai, đoạn văn phải nêu thêm rằng ngay cả những người tin chắc cũng hiếm khi thành công. Nếu không, người đọc có lý do chính đáng để nâng mức tin chắc lên. Phần kiểm chứng cho thấy cách chia này là cần thiết *(Claude đề xuất, phannhatminh chốt)*. Trong pilot có ba tình huống thuộc loại thứ nhất, và ở hai trong số đó, mô hình Qwen2.5-7B gần như không nâng mức tin chắc. Điều này gợi ý rằng phần lớn kết quả mà pilot gọi là "gộp niềm tin với mức tin chắc" có thể đến từ yếu tố gây nhiễu, chứ chưa chắc là lỗi hiểu của mô hình.

Bộ tình huống chính dự kiến có 96 tình huống trên 8 lĩnh vực. Kèm theo đó là 24 tình huống về việc tin vào kết cục xấu để tự thúc đẩy. 24 tình huống của pilot sẽ được dùng làm bộ phát triển.

## 5. Bên nghe được đo bằng nhiều cách hỏi, và các chỉ số chính đều lấy ý người nói làm mốc

Người nghe là người và AI trả lời cùng một bộ câu hỏi. Ba câu hỏi có hoặc không của pilot được giữ lại, và mỗi câu có thêm một cách diễn đạt thứ hai. Kế hoạch thêm hai cách đo *(huysuy05 đề xuất)*:

- Cách thứ nhất yêu cầu bên nghe đưa ra mức tin chắc dưới dạng một con số từ 0 đến 100. Con số này là đại lượng dùng để tính hai khoảng cách ở mục 3.
- Cách thứ hai hỏi thẳng bên nghe rằng người tin giữ niềm tin chủ yếu vì bằng chứng hay chủ yếu vì việc tin có ích. Câu trả lời được so với câu trả lời của người nói cho cùng câu hỏi.

Thước đo lấy từ nghiên cứu của Vesga và cộng sự không còn áp dụng cho AI. Thước đo đó hỏi AI sẽ chọn viết "thinks" hay "believes", nghĩa là nó đặt AI vào vai người nói. Vì AI chỉ làm vai người nghe, thước đo này chỉ được dùng cho nhóm người nói là người, nếu cần *(Claude đề xuất, phannhatminh chốt)*.

Có bốn chỉ số chính:

- Chỉ số thứ nhất là khoảng cách của người nghe là người so với ý người nói *(phannhatminh đề xuất)*.
- Chỉ số thứ hai là khoảng cách của AI so với ý người nói *(phannhatminh đề xuất)*.
- Chỉ số thứ ba là hiệu giữa hai khoảng cách trên, tính theo từng tình huống. Đây là kết quả trung tâm của bài *(phannhatminh đề xuất)*.
- Chỉ số thứ tư là khoảng cách giữa mức tin chắc mà AI gán và con số mà chính văn bản đã nêu. Chỉ số này không cần dữ liệu người *(huysuy05 đề xuất)*.

Mức độ AI khớp với người nghe là người, so với mức các nhóm người nghe khớp với nhau, được giữ lại làm chỉ số phụ *(huysuy05 đề xuất)*.

Kế hoạch chạy trên các mô hình mã nguồn mở thuộc hai đến ba họ khác nhau. Với mỗi họ, kế hoạch lấy cả bản gốc lẫn bản đã được huấn luyện để làm theo chỉ dẫn. Kế hoạch cũng chạy thêm vài mô hình thương mại qua API *(huysuy05 đề xuất)*.

## 6. Phần thu thập dữ liệu từ người là phần nghiên cứu khoa học xã hội của bài

Kế hoạch cần hai nhóm người tham gia, thu qua nền tảng Prolific. Nhóm người nghe gồm khoảng 190 người, với chi phí khoảng 760 đô la theo ước tính của Huy *(huysuy05 đề xuất)*. Nhóm người nói là nhóm mới thêm vào *(phannhatminh đề xuất)*, và kích thước cùng chi phí của nhóm này chưa được ước tính. Người tham gia ở nhóm này không được tham gia nhóm kia. Thiết kế nghiên cứu phải được đăng ký trước. Hội đồng đạo đức nghiên cứu (IRB) phải duyệt cả hai nhóm trước khi thu dữ liệu *(huysuy05 đề xuất)*.

Kế hoạch dùng hai nghiên cứu đã công bố trên người làm bộ kiểm tra bên ngoài. Đó là nghiên cứu của Vesga và cộng sự năm 2025, và nghiên cứu của Cusimano và Lombrozo năm 2021. Mỗi tình huống gốc từ các nghiên cứu này sẽ được chạy song song với một bản diễn đạt lại. Lý do là mô hình có thể đã gặp bản gốc trong dữ liệu huấn luyện *(huysuy05 đề xuất)*.

Bộ dữ liệu WishfulEval chỉ còn một vai trò: làm khuôn mẫu cho câu nói về cảm xúc. Đề xuất so sánh với chính niềm tin của mô hình bị bỏ *(Claude đề xuất, phannhatminh chốt)*. Đề xuất đó đo cách mô hình tự ước lượng xác suất, trong khi dự án đo cách mô hình hiểu niềm tin của người khác.

## 7. Phần phân tích cơ chế đi từ những phương pháp rẻ đến những phương pháp đắt

Toàn bộ phần phân tích cơ chế và phần sửa mô hình là của Huy *(huysuy05 đề xuất)*. Phần này chạy trên hai mô hình Qwen2.5-7B và Llama-3.1-8B ở độ chính xác đầy đủ. Nó dùng bốn phương pháp theo thứ tự:

1. Phương pháp thứ nhất theo dõi câu trả lời hình thành dần qua từng tầng của mô hình.
2. Phương pháp thứ hai lấy trạng thái bên trong từ một đoạn văn và ghép vào đoạn văn kia. Làm vậy cho biết thông tin quyết định câu trả lời nằm ở tầng nào và ở từ nào.
3. Phương pháp thứ ba huấn luyện các bộ phân loại tuyến tính nhỏ. Mục đích là kiểm tra xem trạng thái bên trong có chứa mức tin chắc được nêu và có chứa việc đoạn văn có câu nói việc tin có ích hay không.
4. Phương pháp thứ tư tìm một không gian con nhỏ bên trong mô hình mang thông tin về mức tin chắc (phương pháp DAS). Sau đó nó kiểm tra xem thay đổi không gian con đó có làm câu trả lời thay đổi theo không.

Mục đích của cả bốn bước là trả lời giả thuyết thứ tư. Phần này có thể bắt đầu từ tháng 11 trên các tình huống của pilot, vì nó không cần dữ liệu người.

Nếu khoảng cách của AI lớn hơn rõ rệt so với khoảng cách của người nghe là người, bước cuối cùng là sửa mô hình. Cách sửa là huấn luyện một can thiệp nhỏ đặt đúng tại các vị trí bên trong mô hình mà bước trước đã tìm ra (phương pháp ReFT). Cách sửa này sẽ được so với ba cách khác: đẩy trạng thái bên trong theo một hướng cố định, tinh chỉnh một phần nhỏ trọng số, và đơn giản là viết lại câu lệnh. Bất kỳ cách sửa nào cũng phải thỏa ba điều kiện:

- giữ nguyên mức tin chắc cao ở những tình huống người tin vì bằng chứng;
- không làm giảm kết quả trên bộ kiểm tra niềm tin sai BigToM;
- thu hẹp khoảng cách của AI so với ý người nói trên dữ liệu mà nó chưa từng thấy *(phannhatminh đề xuất)*.

## 8. Có ba mốc quyết định có thể làm bài đổi hướng

Ba mốc, lịch và lựa chọn nơi nộp là của Huy *(huysuy05 đề xuất)*.

- **Mốc thứ nhất, vào cuối tháng 10.** Nhóm thu dữ liệu thử từ một nhóm nhỏ người nói và 9 người nghe. Mốc này giờ phân biệt được hai cách giải thích mà trước đây không tách được *(Claude đề xuất, phannhatminh chốt)*. Giả sử người nghe gán mức tin chắc cao cho Maya. Nếu người nói cũng muốn truyền đạt mức tin chắc cao, thì khung lý thuyết cần sửa. Nếu người nói muốn truyền đạt mức tin chắc thấp, thì đó là một khoảng hở thật trong giao tiếp giữa người với người, và câu hỏi về AI được đặt so với khoảng hở đó.
- **Mốc thứ hai, vào giữa tháng 2.** Nhóm xem dữ liệu đầy đủ có cho thấy khoảng cách của AI khác rõ rệt so với khoảng cách của người nghe là người hay không. Nếu AI lệch nhiều hơn, nhóm làm phần sửa mô hình. Nếu không, bài báo cáo hai khoảng cách và giải thích cơ chế bên trong.
- **Mốc thứ ba, vào giữa tháng 3.** Nhóm chọn nơi nộp bài.

Nơi nộp ưu tiên là nhánh Evaluations & Datasets của hội nghị NeurIPS, hạn khoảng đầu tháng 5. Phần phân tích cơ chế được gửi thêm tới workshop về diễn giải cơ chế tại hội nghị ICML. Phương án dự phòng là chu kỳ tháng 5 của ACL Rolling Review.

## 9. Trong hai tuần tới có bảy việc cụ thể cần làm

1. *(phannhatminh đề xuất)* Thiết kế biểu mẫu cho người nói, trong đó sự thật về nhân vật được viết bằng ngôn ngữ không chứa chữ "believe".
2. *(phannhatminh đề xuất)* Thu dữ liệu thử từ một nhóm nhỏ người nói và từ 9 người nghe, dùng biểu mẫu hiện có cho người nghe.
3. *(huysuy05 đề xuất)* Nộp hồ sơ lên hội đồng đạo đức nghiên cứu cho cả hai nhóm người tham gia.
4. *(huysuy05 đề xuất)* Tải các tình huống của Vesga và của Cusimano từ kho OSF, rồi chạy hai mô hình của pilot trên các tình huống đó.
5. *(huysuy05 đề xuất)* Viết lại tệp `pilot/stimuli.py` theo tám phiên bản và hai loại câu nói việc tin có ích.
6. *(huysuy05 đề xuất)* Chạy lại pilot trên Qwen2.5-7B ở độ chính xác đầy đủ và làm lượt ghép trạng thái bên trong đầu tiên.
7. *(huysuy05 đề xuất)* Cập nhật `README.md` và `note.md` theo phạm vi mới.

Kế hoạch gợi ý chia công việc thành hai nhánh chạy song song *(huysuy05 đề xuất)*. Một người phụ trách bộ đánh giá và phần nghiên cứu trên người, người kia phụ trách phần phân tích cơ chế.
