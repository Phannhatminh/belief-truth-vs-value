# Hướng đi của dự án

Ngày cập nhật: 27/9/2026. Đây là bản hướng đi đầy đủ mà phannhatminh và huysuy05 dùng để thống nhất kế hoạch từ nay. Bản này bao gồm toàn bộ nội dung thiết kế của `revised_plan_believe.md` (commit 45a3d97). Nó có thêm thiết kế ba bên gồm người nói, người nghe là người và AI (mục 3), cùng các điều chỉnh rút ra từ phần kiểm chứng.

## Cách đọc tài liệu này

Mỗi ý được gắn nhãn theo người đề xuất:

- Nhãn *(phannhatminh đề xuất)* chỉ ý của phannhatminh.
- Nhãn *(phannhatminh đề xuất, note.md)* chỉ ý đã có trong `note.md` từ trước khi có kế hoạch của Huy.
- Nhãn *(huysuy05 đề xuất)* chỉ ý của huysuy05, lấy từ `revised_plan_believe.md`.
- Nhãn *(Claude đề xuất, phannhatminh chốt)* chỉ những ý do Claude đưa ra trong lúc kiểm chứng và trao đổi, sau đó được phannhatminh chốt vào tài liệu.

Những chỗ tài liệu này khác với kế hoạch của Huy được đánh dấu **[Khác kế hoạch của Huy]**. Những chỗ Claude cho rằng kế hoạch của Huy sai về dữ kiện, hoặc cần làm rõ, được đánh dấu **[Claude sửa]**. Ở mỗi chỗ đó, lời gốc của Huy được giữ nguyên trong ngoặc «», và mục 13 nêu rõ Claude cho là sai ở đâu, sửa thành gì và vì sao. Những chỗ hai người cần quyết định cùng nhau được đánh dấu **[Cần thống nhất]**. Mục 12 liệt kê lại tất cả các chỗ cần thống nhất.

## 1. Câu hỏi nghiên cứu giữ nguyên, nhưng hình thức của bài thay đổi

Câu hỏi gốc vẫn như cũ *(phannhatminh đề xuất)*. Khi một câu "X believes that p" giữ nguyên từng chữ và chỉ đoạn văn phía trước thay đổi, chữ "believe" được hiểu theo cách nào?

Bài đặt câu hỏi này thành một câu hỏi về giao tiếp *(phannhatminh đề xuất)*. Người nói dùng chữ "believe" với một ý định cụ thể. Ý định đó đến được người nghe là người nhiều đến đâu, và đến được AI nhiều đến đâu khi AI làm việc nghe và hiểu? **[Khác kế hoạch của Huy]** Kế hoạch của Huy lấy phán đoán của người nghe làm đáp án tham chiếu, còn tài liệu này lấy ý của người nói làm mốc chung.

Bài gồm hai phần *(huysuy05 đề xuất)*:

- phần đầu là một bộ đánh giá chuẩn (benchmark), có dữ liệu từ người thật;
- phần sau phân tích cơ chế bên trong mô hình.

Huy đưa ra lý do cho hình thức này như sau. Ở những tình huống quan trọng nhất, chưa ai biết chắc câu trả lời đúng, nên phán đoán của người thật phải làm đáp án tham chiếu. Việc thu các phán đoán đó tự nó đã là nghiên cứu khoa học xã hội, nên bộ đánh giá và nghiên cứu khoa học xã hội là một bài. Mục tiêu là nộp bài vào khoảng tháng 5 năm 2027.

Bài dự kiến có năm đóng góp *(huysuy05 đề xuất)*:

1. Đóng góp thứ nhất là một bộ đánh giá có dữ liệu từ người, có biến cảm xúc và các chỉ số ở mục 5.
2. Đóng góp thứ hai là kết quả đánh giá trên nhiều mô hình.
3. Đóng góp thứ ba là việc cho mô hình lặp lại hai nghiên cứu trên người đã công bố.
4. Đóng góp thứ tư là kết quả phân tích cơ chế trên hai mô hình.
5. Đóng góp thứ năm là một cách sửa mô hình, nếu Mốc 2 cho thấy có khoảng chênh.

Nếu muốn một bài thuần khoa học xã hội, nhóm bỏ đóng góp thứ tư và thứ năm, và nhắm tới CogSci hoặc một tạp chí.

Ba phần sau được chuyển sang hướng làm sau vì không kịp trước tháng 5 *(huysuy05 đề xuất)*. Phần thứ nhất là ngôn ngữ hình thức cho belief và acceptance. Phần thứ hai là belief-in. Phần thứ ba là mẫu tự nhiên lấy từ corpus. Ba phần này ứng với `note.md` mục A1 đến A4 và phần lớn mục §8.

## 2. Khung lý thuyết có ba cách hiểu chữ "believe" và bốn giả thuyết

Kế hoạch giữ nguyên hai cách hiểu mà dự án đã có từ đầu *(phannhatminh đề xuất, note.md)*:

- Theo cách hiểu thứ nhất, một người tin điều gì đó vì bằng chứng cho thấy điều đó đúng.
- Theo cách hiểu thứ hai, một người tin điều gì đó vì việc tin giúp họ có kết cục tốt hơn, dù họ biết khả năng điều đó xảy ra là thấp.

Kế hoạch của Huy thêm một cách hiểu thứ ba *(huysuy05 đề xuất)*. Theo cách hiểu thứ ba, một người tin điều gì đó vì họ mong nó xảy ra, và mong muốn đó khiến họ đánh giá khả năng xảy ra cao hơn mức bằng chứng cho phép. Cách hiểu thứ ba này thường được gọi là wishful thinking.

Trong tài liệu này, "mức tin chắc" là xác suất mà chính người tin tự đánh giá cho điều họ tin. Theo khung ba cách hiểu, kết quả của pilot có một cách diễn giải mới *(huysuy05 đề xuất)*. Mô hình gán mức tin chắc cao cho người tin theo cách hiểu thứ hai, vậy là mô hình đã hiểu họ theo cách hiểu thứ ba.

Huy dẫn bốn nguồn bằng chứng cho vai trò của cảm xúc *(huysuy05 đề xuất)*:

- Ở người, sợ hãi làm phán đoán rủi ro bi quan hơn, còn tức giận làm nó lạc quan hơn (Lerner và Keltner 2001).
- Mong muốn một kết cục làm tăng khả năng người ta dự đoán kết cục đó sẽ xảy ra (Krizan và Windschitl 2007).
- Vesga và cộng sự (2025) xếp điều hòa cảm xúc vào các chức năng của niềm tin không nhằm vào sự thật.
- Ở mô hình, kế hoạch của Huy viết: «Yongsatianchot và Marsella [5] thấy wishful thinking trong ước lượng xác suất của chính mô hình. Hiện tượng này xuất hiện chủ yếu khi prompt có câu "You feel really hopeful about the outcome."» **[Claude sửa]** Claude cho rằng câu này sai ở hai chỗ, và sửa như sau: wishful thinking trong bài đó chỉ xuất hiện khi mô hình nhập vai một nhân vật, không xuất hiện trong ước lượng của chính mô hình; câu "hopeful" chỉ cần thiết ở miền bài toán logic, còn ở miền thể thao, hai mô hình đã có thiên lệch mà không cần câu đó. Chi tiết ở mục 13, chỗ sửa thứ nhất.

Kế hoạch đặt ra bốn giả thuyết *(huysuy05 đề xuất)*.

**Giả thuyết thứ nhất là mô hình thổi phồng mức tin chắc.** Theo bản của Huy, so với người đọc, mô hình gán mức tin chắc cao hơn cho người tin theo cách hiểu thứ hai. Điều này rõ nhất khi lợi ích của việc tin rơi vào một kết cục khác với điều được tin, hoặc khi mức tin chắc thấp của người tin được nêu rõ. **[Khác kế hoạch của Huy]** Theo thiết kế ba bên, giả thuyết này được viết lại như sau: AI gán cho người tin theo cách hiểu thứ hai một mức tin chắc cao hơn mức mà người nói muốn truyền đạt, và độ lệch này lớn hơn độ lệch của người nghe là người *(phannhatminh đề xuất)*. **[Cần thống nhất]** Hai người cần chọn bản nào là giả thuyết chính.

**Giả thuyết thứ hai là về cảm xúc.** Với người đọc, chữ "believes" đứng sau một câu về sợ hãi sẽ được hiểu theo cách thứ hai, tức mức tin chắc vẫn thấp. Đứng sau một câu về hy vọng, nó sẽ được hiểu theo cách thứ ba, tức mức tin chắc tăng lên. Còn mô hình thì chỉ bám theo sắc thái tích cực hay tiêu cực của từ chỉ cảm xúc: hy vọng làm mức tin chắc tăng, sợ hãi làm mức tin chắc giảm, bất kể đoạn văn có câu nói việc tin có ích hay không. Vì vậy hiệu ứng cảm xúc ở mô hình và ở người sẽ lệch nhau tại những phiên bản có câu nói việc tin có ích.

**Giả thuyết thứ ba là về sắc thái so với chức năng.** Trong các tình huống bi quan phòng vệ, niềm tin có ích lại là một niềm tin vào kết cục xấu. Ví dụ là một sinh viên tin rằng mình sẽ trượt để tiếp tục ôn bài (Norem và Cantor 1986). Mô hình nào đồng nhất "tin" với "hy vọng" sẽ gán sai mức tin chắc ở các tình huống này, còn người thì không.

**Giả thuyết thứ tư là về cơ chế.** Khi mô hình hiểu lệch, có hai khả năng. Khả năng thứ nhất là gộp ở mức biểu diễn: bên trong mô hình không có một biến riêng cho mức tin chắc của người tin. Khả năng thứ hai là gộp ở mức đọc ra: mô hình có mã hóa xác suất được nêu, nhưng câu trả lời cho câu hỏi "thinks it is likely" lại bị câu tường thuật niềm tin chi phối. Mục 7 được thiết kế để phân biệt hai khả năng này.

## 3. Thiết kế có ba bên: người nói, người nghe là người, và AI làm vai người nghe

Toàn bộ mục này là phần thêm vào so với kế hoạch của Huy. **[Khác kế hoạch của Huy]**

Mỗi câu "X believes that p" liên quan đến ba vai. Vai thứ nhất là người tin, ví dụ Maya. Vai thứ hai là người nói, tức người dùng câu đó để mô tả Maya. Vai thứ ba là người nghe, tức người đọc câu đó và tự hiểu Maya tin gì. Người nói và người nghe có thể hiểu cùng một câu theo hai cách khác nhau. Trong dự án này, AI luôn làm vai người nghe *(phannhatminh đề xuất)*.

**Cách hiểu của người nói được thu từ người thật, không lấy từ nhóm nghiên cứu.** Trước đây, ý người nói chính là nhãn mà nhóm nghiên cứu gán khi viết đoạn văn. Giờ một nhóm người tham gia riêng sẽ đóng vai người nói *(phannhatminh đề xuất)*. Người nói được biết đầy đủ sự thật về nhân vật, và sự thật đó được viết bằng ngôn ngữ không chứa chữ "believe". Ví dụ, họ được biết rằng Maya tự đánh giá cơ hội thành công khoảng một phần mười, và Maya chọn giữ thái độ tin tưởng vì thái độ đó giúp cô hồi phục tốt hơn. Sau đó người nói trả lời ba câu hỏi *(Claude đề xuất, phannhatminh chốt)*:

1. Câu thứ nhất hỏi họ có chấp nhận mô tả Maya bằng câu đích, ví dụ "Maya believes that the surgery will succeed", hay không.
2. Câu thứ hai hỏi khi dùng câu đó, họ muốn người nghe hiểu Maya tin chắc đến đâu.
3. Câu thứ ba hỏi họ muốn người nghe hiểu Maya tin vì bằng chứng hay vì việc tin có ích.

Nhờ quy trình này, câu đích vẫn giữ nguyên từng chữ. Phương pháp luận chi tiết cho phần người nói, ở trạng thái đề xuất, nằm trong `problem1/methodology.md`.

**Người nghe là người và AI nhận cùng một đầu vào.** Cả hai đọc đoạn văn kèm câu đích và trả lời cùng các câu hỏi ở mục 5. Như vậy mỗi tình huống có ba con số về mức tin chắc: con số người nói muốn truyền đạt, con số người nghe là người hiểu được, và con số AI hiểu được.

**Phép so chính là so hai khoảng cách với cùng một mốc là ý người nói.** *(phannhatminh đề xuất)* Với mỗi tình huống, gọi s là mức tin chắc mà người nói muốn truyền đạt, h là mức tin chắc mà người nghe là người hiểu được, và m là mức tin chắc mà AI hiểu được. Khoảng cách của người nghe là h trừ s. Khoảng cách của AI là m trừ s. Hiệu giữa hai khoảng cách được tính trên từng tình huống rồi kiểm định theo cặp *(Claude đề xuất, phannhatminh chốt)*. Bài giữ cả dấu của khoảng cách, không chỉ lấy độ lớn. Dấu cho biết bên nghe hiểu mức tin chắc cao hơn hay thấp hơn ý người nói.

**Cách so này bỏ được giả định rằng người nghe là người luôn đúng.** *(Claude đề xuất, phannhatminh chốt)* Khi đáp án là người nghe, AI chỉ có thể khớp với người nghe hoặc kém hơn người nghe. Khi mốc so là ý người nói, AI có thể kém hơn người nghe, ngang bằng người nghe, hoặc hiểu đúng ý người nói hơn cả người nghe.

**Có hai điểm phải thiết kế cẩn thận để phép so công bằng.** *(Claude đề xuất, phannhatminh chốt)*

- Điểm thứ nhất là người nghe là người gồm nhiều cá nhân, còn AI chỉ cho một câu trả lời. Nếu lấy trung bình của nhiều người nghe, nhiễu cá nhân bị triệt tiêu và phép so sẽ nghiêng về phía người. Vì vậy bài xếp khoảng cách của AI vào phân bố khoảng cách của từng người nghe riêng lẻ.
- Điểm thứ hai là người nói cũng không nhất trí với nhau. Vì vậy s được xử lý như một phân bố chứ không phải một con số. Ở những tình huống mà người nói bất đồng nhiều, bản thân tình huống đã mơ hồ, nên khoảng cách của cả hai bên nghe ở đó phải được đọc thận trọng.

## 4. Bộ tình huống được viết lại để loại bỏ những yếu tố gây nhiễu mà pilot mắc phải

Toàn bộ thiết kế tình huống trong mục này là của Huy *(huysuy05 đề xuất)*, trừ những chỗ ghi nhãn khác.

**Pilot có ba điểm yếu về tình huống.** Điểm yếu thứ nhất là câu nói việc tin có ích thường làm thay đổi chính xác suất của điều được tin. Ở 21 trong 24 tình huống, câu đó nói rằng việc tin làm tăng khả năng điều được tin xảy ra, hoặc trực tiếp (Kenji đánh tốt hơn) hoặc qua nỗ lực (Farid tiếp tục tưới nước). Người đọc hiểu câu đó theo nghĩa đen thì nên đánh giá cơ hội cao hơn tỷ lệ nền, nên một phần mức tin chắc cao mà mô hình gán có thể là suy luận đúng. Chỉ ba tình huống của Maya, Leila và Ingrid có câu nói việc tin cải thiện một kết cục khác. Điểm yếu thứ hai là mức tin chắc của chính người tin chưa bao giờ được nêu, vì các đoạn văn chỉ nêu xác suất khách quan. Điểm yếu thứ ba là cảm xúc chưa được thao tác, nên sức nặng cảm xúc bị lẫn với lĩnh vực.

Phần kiểm chứng xác nhận các con số của Huy *(Claude đề xuất, phannhatminh chốt)*. Trên Qwen2.5-7B, mức dịch mức tin chắc khi thêm câu nói việc tin có ích là +0,48 ở nhóm 21 tình huống và +0,20 ở nhóm 3 tình huống. Trong nhóm 3 tình huống, hai tình huống Maya và Leila gần như không dịch, và toàn bộ mức +0,20 đến từ Ingrid. Điều này gợi ý rằng phần lớn kết quả mà pilot gọi là "gộp niềm tin với mức tin chắc" có thể đến từ yếu tố gây nhiễu.

**Mỗi tình huống có sáu thành phần.** Các thành phần là phần mở đầu, điều được tin, bằng chứng mạnh hoặc yếu, một câu nói việc tin có ích, một câu về cảm xúc, và một câu nêu mức tin chắc. Câu đích giữ nguyên qua mọi phiên bản.

**Câu nói việc tin có ích thuộc một trong hai loại.**

- Ở loại gián tiếp, việc tin cải thiện một kết cục khác với điều được tin. Ví dụ, việc tin giúp Maya hồi phục tốt hơn sau mổ.
- Ở loại tự hiện thực hóa, việc tin làm tăng xác suất của chính điều được tin. Các tình huống loại này phải nêu thêm xác suất trong nhóm những người tin, ví dụ "even fighters who go in convinced win only about one time in ten from his position".

**Câu về cảm xúc chỉ gọi tên một cảm xúc và không nói gì về xác suất.** Ví dụ là "Maya feels hopeful." hoặc "Maya feels frightened.". **Câu nêu mức tin chắc tường thuật ước lượng của chính người tin.** Ví dụ là "Asked to put a number on it, Maya says her chances are about one in ten.".

**Mỗi tình huống có tám phiên bản.**

1. Phiên bản TS có bằng chứng mạnh, không có câu nói việc tin có ích, không có câu cảm xúc và không nêu mức tin chắc. Nó là mốc neo.
2. Phiên bản IR có bằng chứng yếu và không có ba câu kia. Nó thể hiện niềm tin đi ngược bằng chứng.
3. Phiên bản IR-H là IR cộng câu về hy vọng. Nó thể hiện wishful thinking.
4. Phiên bản IR-F là IR cộng câu về sợ hãi. Nó thể hiện cảm xúc khi không có lợi ích từ việc tin.
5. Phiên bản VD là IR cộng câu nói việc tin có ích. Nó là điều kiện của pilot.
6. Phiên bản VD-H là VD cộng câu về hy vọng. Nó dùng để kiểm tra giả thuyết thứ hai.
7. Phiên bản VD-F là VD cộng câu về sợ hãi. Nó cũng dùng để kiểm tra giả thuyết thứ hai.
8. Phiên bản VD-K là VD cộng câu nêu mức tin chắc. Nó là phép thử rõ ràng nhất cho giả thuyết thứ nhất.

**Quy mô bộ tình huống.** Bộ lõi gồm 96 tình huống trên 8 lĩnh vực, một nửa thuộc loại gián tiếp và một nửa thuộc loại tự hiện thực hóa. Kèm theo đó là 24 tình huống bi quan phòng vệ, chỉ ở các phiên bản TS, IR, VD và VD-K.

**Bộ phát triển và đối chứng từ vựng.** 24 tình huống của pilot, sau khi viết lại, trở thành bộ phát triển cùng với hai đối chứng từ vựng VDn và IRf. Pilot đã cho thấy thêm một câu trung tính không làm mức tin chắc tăng, nên hai đối chứng này không cần thu dữ liệu người ở quy mô đầy đủ.

**Cách viết tình huống.** Có thể dùng LLM viết nháp từ khuôn mẫu, với hai điều kiện. Điều kiện thứ nhất là cả hai tác giả sửa từng tình huống. Điều kiện thứ hai là có một vòng kiểm định nhỏ trước khi thu dữ liệu người.

## 5. Các thước đo, chỉ số và bộ mô hình

**Câu hỏi và thước đo.** *(huysuy05 đề xuất)* Ba câu hỏi có hoặc không của pilot được giữ lại, và mỗi câu có hai cách diễn đạt. Kế hoạch thêm ba loại thước đo:

- Loại thứ nhất là mức tin chắc dạng số, ví dụ "What chance does Maya think the surgery has, from 0 to 100?". Đây là thước đo liên tục, và dùng được cho các mô hình API không trả log-probability. Theo thiết kế ba bên, con số này cũng là đại lượng dùng để tính hai khoảng cách ở mục 3 *(phannhatminh đề xuất)*.
- Loại thứ hai là một câu hỏi phân loại tường minh, ví dụ "Does Maya hold this belief mainly because of the evidence, or mainly because believing helps her?". Câu này cho biết bên nghe có gọi tên được cách hiểu hay không. Theo thiết kế ba bên, câu trả lời được so với câu trả lời của người nói cho cùng câu hỏi *(phannhatminh đề xuất)*.
- Loại thứ ba là hai thước đo đặc trưng của Vesga và cộng sự, đọc từ log-probability tại vị trí động từ. Thước đo thứ nhất so "thinks" với "believes". Thước đo thứ hai so "decided to believe" với "decided whether to believe". Người ta ưu tiên "thinks" và "decided whether" cho niềm tin nhằm vào sự thật. Vì hai thước đo này không cần câu hỏi, chúng chấm được cả mô hình gốc lẫn mô hình đã huấn luyện theo chỉ dẫn. **[Khác kế hoạch của Huy]** Hai thước đo này hỏi AI sẽ chọn viết từ nào, nghĩa là chúng đặt AI vào vai người nói. Vì AI chỉ làm vai người nghe, tài liệu này chỉ dùng chúng cho người nói là người *(Claude đề xuất, phannhatminh chốt)*. **[Cần thống nhất]**

**Ba chỉ số chính của Huy.** *(huysuy05 đề xuất)* Gọi m là mức tin chắc mà mô hình gán và h là điểm trung bình của người nghe, cả hai quy về khoảng từ 0 đến 1. Vì đáp án chuẩn còn tranh cãi, cả ba chỉ số được định nghĩa tương đối so với người ở mọi chỗ có thể.

- **Chỉ số thổi phồng mức tin chắc (CI)** lấy mức mô hình dịch mức tin chắc từ IR sang VD, trừ đi mức người dịch, rồi lấy trung bình qua các tình huống. Chỉ số bằng 0 nghĩa là khi thêm câu nói việc tin có ích, mô hình dịch đúng bằng mức người dịch. Chỉ số dương nghĩa là mô hình dịch nhiều hơn. Chỉ số được báo cáo riêng cho loại gián tiếp và loại tự hiện thực hóa. Riêng phần của mô hình trong pilot là +0,44 với Qwen2.5-7B.
- **Chỉ số sai số so với mức tin chắc được nêu (SCE)** lấy mức tin chắc mà mô hình gán ở phiên bản VD-K trừ đi con số mà văn bản nêu, rồi lấy trung bình. Chỉ số này không cần dữ liệu người. Kèm theo là tỷ lệ tình huống VD-K mà mô hình trả lời Yes cho câu "thinks it is likely". Đánh giá của người ở VD-K dùng để kiểm tra rằng người đọc chấp nhận con số được nêu.
- **Chỉ số khớp với người (HA)** là tương quan Spearman giữa mô hình và người trên các ô tình huống nhân phiên bản, chia cho trần nhiễu của người. Trần nhiễu được tính từ tương quan giữa hai nửa ngẫu nhiên của nhóm người đánh giá.

**Các chỉ số khoảng cách của thiết kế ba bên.** *(phannhatminh đề xuất)* **[Khác kế hoạch của Huy]**

- Chỉ số thứ nhất là khoảng cách của người nghe là người so với ý người nói.
- Chỉ số thứ hai là khoảng cách của AI so với ý người nói.
- Chỉ số thứ ba là hiệu giữa hai khoảng cách trên, tính theo từng tình huống.

**[Cần thống nhất]** Hai người cần quyết định chỉ số nào là kết quả trung tâm của bài: CI của Huy, hay hiệu giữa hai khoảng cách của thiết kế ba bên. CI so mô hình với người nghe. Hiệu giữa hai khoảng cách so cả mô hình lẫn người nghe với người nói. Hai chỉ số có thể cùng được báo cáo.

**Ba chỉ số chẩn đoán.** *(huysuy05 đề xuất)*

- **Độ nhạy với cảm xúc** được tính riêng cho hy vọng và cho sợ hãi. Nó lấy mức mô hình dịch từ VD sang VD có cảm xúc, trừ đi mức người dịch. Nó được tính ở cả các phiên bản có và không có câu nói việc tin có ích.
- **Khoảng chênh đặc trưng** là hiệu log-probability giữa "thinks" và "believes" trong từng phiên bản. Nếu mô hình theo đúng khuôn mẫu của người, khoảng chênh ở TS sẽ lớn hơn ở VD. **[Khác kế hoạch của Huy]** Chỉ số này đặt AI vào vai người nói, nên phụ thuộc vào quyết định ở trên về thước đo của Vesga.
- **Khoảng chênh tường minh và ngầm** là độ chính xác của câu hỏi phân loại tường minh, trừ đi mức trùng với đa số người ở câu hỏi mức tin chắc. Một mô hình gọi đúng tên cách hiểu thứ hai mà vẫn gán mức tin chắc cao là mô hình có thông tin nhưng không dùng. Đây là lý do về mặt hành vi để làm mục 7.

**Độ bền và kiểm định.** *(huysuy05 đề xuất)* Độ bền được báo cáo qua phương sai giữa các cách diễn đạt câu hỏi, và qua kết quả trên các lĩnh vực giữ lại. Hiệu ứng ở người được kiểm định bằng mô hình hỗn hợp, với hiệu ứng ngẫu nhiên cho người tham gia và cho tình huống. Các so sánh trên mô hình dùng kiểm định cặp theo tình huống và khoảng tin cậy bootstrap như trong `pilot/analyze.py`.

**Bộ mô hình.** *(huysuy05 đề xuất)*

- Nhóm chạy các cặp mô hình gốc và mô hình đã huấn luyện theo chỉ dẫn, ở hai hoặc ba kích cỡ, từ hai hoặc ba họ mô hình mở như Qwen, Llama và OLMo. Dữ liệu huấn luyện mở của OLMo giúp trả lời câu hỏi về nhiễm dữ liệu.
- Ít nhất một mô hình được chạy thêm ở bf16 để kiểm tra lại kết quả của bản lượng tử hóa 4-bit.
- Nhóm chạy thêm hai đến bốn mô hình API, chấm qua câu trả lời dạng số và lấy mẫu.

## 6. Dữ liệu từ người và dữ liệu có sẵn

**Dữ liệu người nghe.** *(huysuy05 đề xuất)* Nhóm dùng Latin square trên 8 danh sách, và mỗi người đọc 24 đoạn, mất khoảng 15 phút. Mỗi ô tình huống nhân phiên bản cần ít nhất 5 đánh giá, nên cần 96 × 8 × 5 / 24 = 160 người. Sau khi loại khoảng 15%, con số là khoảng 190 người. Với mức 16 đô la mỗi giờ-người, tổng chi phí khoảng 760 đô la. Thiết kế, tiêu chí loại người tham gia và các phép so sánh chính nên được đăng ký trước. `pilot/build_form.py` và khuôn biểu mẫu hiện có có thể mở rộng cho việc này bằng cách thêm danh sách.

**Dữ liệu người nói.** *(phannhatminh đề xuất)* **[Khác kế hoạch của Huy]** Nhóm người nói là nhóm mới thêm vào, và kích thước cùng chi phí của nhóm này chưa được ước tính. Người tham gia ở nhóm này không được tham gia nhóm kia. **[Cần thống nhất]** Hai người cần quyết định người nói có dùng cùng 8 danh sách Latin square với người nghe không, và mỗi ô cần bao nhiêu người nói.

**IRB.** *(huysuy05 đề xuất)* Đánh giá của người dự định công bố thường cần được hội đồng đạo đức nghiên cứu duyệt trước khi thu. Vì vậy vòng thu dữ liệu nhỏ ở Mốc 1 chỉ nên coi là kiểm tra nội bộ cho các tình huống. Hồ sơ IRB cho nghiên cứu đầy đủ nên được nộp ngay trong tháng 10, và phải bao gồm cả hai nhóm người tham gia.

**Nghiên cứu của Vesga, Van Leeuwen và Lombrozo (2025) là bộ kiểm tra chuyển giao.** *(huysuy05 đề xuất)* Đây là ba nghiên cứu đã đăng ký trước, với số người sau khi loại là 383, 723 và 740, về cách người gán niềm tin nhằm vào sự thật và niềm tin không nhằm vào sự thật. Tình huống, dữ liệu và mã phân tích đều có trên OSF (dự án 38YGN). Nhóm có thể cho mô hình làm người tham gia trên đúng các tình huống gốc, rồi so với kết quả đã công bố. Kế hoạch của Huy viết: «niềm tin non-epistemic của họ phục vụ bản sắc, lòng trung thành và điều hòa cảm xúc, chứ không nhằm một kết cục tốt hơn». **[Claude sửa]** Claude cho rằng danh sách chức năng này không khớp với bài gốc, và sửa như sau: bốn cặp tình huống của họ xoay quanh lòng trung thành, đức tin tôn giáo, cam kết đạo đức và bản sắc; điều hòa cảm xúc chỉ được nhắc như một ví dụ chung trong phần tóm tắt, không có tình huống riêng. Chi tiết ở mục 13, chỗ sửa thứ hai. Kết luận của Huy vẫn giữ nguyên: không tình huống nào có cấu trúc "tin để kết cục tốt hơn", nên đây là bộ kiểm tra chuyển giao chứ không phải bộ lõi.

**Nghiên cứu của Cusimano và Lombrozo (2021) là bộ kiểm tra bên ngoài thứ hai.** *(huysuy05 đề xuất)* Họ đặt bằng chứng đối lập với lợi ích đạo đức hoặc thực tiễn của việc tin. Một tình huống của họ có đúng cấu trúc của loại gián tiếp: người chồng bị ung thư, chỉ 15% số người mắc bệnh sống quá một năm, và sự lạc quan giúp cả gia đình sống tốt hơn. Kế hoạch của Huy viết: «Các nghiên cứu của họ (N = 839 và 1.021)». **[Claude sửa]** Claude cho rằng con số này thiếu một nghiên cứu, và bổ sung như sau: bài có ba nghiên cứu, với mẫu phân tích lần lượt là 839, 1.021 và 233 người. Chi tiết ở mục 13, chỗ sửa thứ ba. Họ đo niềm tin mà người ta cho là nhân vật nên có, so với khoảng mà bằng chứng cho phép, và đo các phán đoán về tính chính đáng và về tri thức. Tình huống và dữ liệu có trên OSF. Đây là dữ liệu người đã công bố gần nhất với cách hiểu thứ hai.

**WishfulEval chỉ còn vai trò khuôn mẫu cho câu về cảm xúc.** Kế hoạch của Huy viết rằng bộ này «kết hợp mức mong muốn kết cục với độ mạnh của bằng chứng trong các bài ước lượng xác suất», và có sẵn thao tác "hopeful" *(huysuy05 đề xuất)*. **[Claude sửa]** Claude không cho rằng câu này sai, mà chỉ ghi thêm thuật ngữ của bài gốc: biến thứ hai trong bài là độ bất định của thông tin. Chi tiết ở mục 13, chỗ sửa thứ tư. **[Khác kế hoạch của Huy]** Kế hoạch của Huy đề xuất thêm một phép so sánh ngôi thứ nhất: wishful thinking của chính mô hình có dự đoán được điều nó gán cho người khác không. Đề xuất này bị bỏ vì hai lý do *(Claude đề xuất, phannhatminh chốt)*. Lý do thứ nhất là bài gốc không có wishful thinking ở ngôi thứ nhất, vì hiện tượng chỉ xuất hiện khi nhập vai. Lý do thứ hai là đề xuất đó đo cách mô hình tự ước lượng xác suất, trong khi dự án đo cách mô hình hiểu niềm tin của người khác.

**Kiểm tra nhiễm dữ liệu.** *(huysuy05 đề xuất)* Các tình huống đã công bố của ba nguồn trên có thể nằm trong dữ liệu huấn luyện. Vì vậy mỗi bản gốc được chạy song song với một bản diễn đạt lại.

**Corpus mental-spaces của Steele, Wen và Han làm đối chứng dương cho phần cơ chế.** *(phannhatminh đề xuất, note.md)* Huy nhắc lại ý này trong kế hoạch của mình.

**Ba corpus trông hứa hẹn nhưng không phù hợp.** *(huysuy05 đề xuất)*

- GoEmotions có 54.263 bình luận, trong đó chỉ 457 bình luận có một dạng của động từ "believe". Huy đếm được 15 bình luận dùng khung chủ ý như "choose to", "need to" hoặc "want to believe". **[Claude sửa]** Claude đếm ba khung đó được 11 bình luận, và không tìm được cách đếm nào ra đúng 15. Chi tiết ở mục 13, chỗ sửa thứ năm. Kết luận không đổi: số lượng quá ít để dùng.
- CommitmentBank có 74 tình huống với "believe", nhưng tất cả đều nằm dưới phủ định, câu hỏi, động từ khuyết thiếu hoặc câu điều kiện. Chúng được chấm theo mức cam kết của người nói, không theo loại niềm tin. Phần kiểm chứng xác nhận hai con số này.
- EmpatheticDialogues có 32 nhãn cảm xúc, trong đó có hopeful, faithful và anxious, nên có thể cung cấp mẫu tự nhiên. Số tình huống chứa "believe" trong bộ này chưa được đếm. Dữ liệu tự nhiên được để sau tháng 5.

## 7. Phần phân tích cơ chế có hai câu hỏi chính: mỗi cách hiểu được biểu diễn bên trong AI như thế nào, và khi AI hiểu lệch thì lỗi nằm ở đâu

Phần này có hai câu hỏi chính ngang hàng nhau. Câu hỏi thứ nhất hỏi về biểu diễn khi AI hiểu đúng. Câu hỏi thứ hai hỏi về chỗ hỏng khi AI hiểu lệch.

**Câu hỏi chính thứ nhất là: khi AI hiểu chữ "believe", mỗi cách hiểu được biểu diễn bên trong AI như thế nào?** *(phannhatminh đề xuất, note.md)* Câu hỏi này có hai tầng, và cả hai tầng đã được đặt ra ở `note.md` §2. Tầng thứ nhất hỏi các cách hiểu có tách nhau trong trạng thái bên trong của mô hình hay không. Tầng thứ hai hỏi mô hình có thật sự dùng sự phân biệt đó khi suy luận hay không.

**Cụm "khi AI hiểu" được xác định bằng thiết kế ba bên.** *(Claude đề xuất, phannhatminh chốt)* Ở những tình huống mà câu trả lời của AI khớp với ý người nói, nhóm có cơ sở để nói AI hiểu, và việc phân tích biểu diễn ở đó là có nghĩa. Ở những tình huống AI hiểu lệch, việc so biểu diễn giữa hai nhóm tình huống cho biết cái gì bị thiếu. Nhãn cách hiểu dùng để huấn luyện bộ phân loại được lấy từ câu trả lời của người nói, không lấy từ nhãn mà nhóm nghiên cứu gán khi viết đoạn văn.

**Câu trả lời có thể rơi vào hai dạng khác nhau về bản chất, và việc phân biệt hai dạng này tự nó đã là một phát hiện.** *(Claude đề xuất, phannhatminh chốt)*

- Ở dạng thứ nhất, mô hình có một biến trừu tượng cho "loại niềm tin". Nếu dạng này đúng, sẽ tồn tại một hướng hoặc một không gian con nhỏ tách ba cách hiểu, và biến đó tổng quát được sang những lĩnh vực mà bộ phân loại chưa từng thấy.
- Ở dạng thứ hai, mô hình không có biến như vậy mà chỉ theo dõi từng thành phần riêng lẻ. Các thành phần đó là mức tin chắc, việc niềm tin có đi theo bằng chứng hay không, và việc tin có mang lại lợi ích hay không. Theo dạng này, một cách hiểu chỉ là một tổ hợp của các thành phần.

Phép thử để tách hai dạng như sau. Nhóm tìm không gian con mang loại niềm tin bằng phương pháp DAS, rồi hoán đổi không gian con đó giữa hai đoạn văn. Nếu mô hình có một biến thống nhất, việc hoán đổi sẽ làm mọi câu trả lời đổi cùng lúc, gồm mức tin chắc, khả năng bỏ niềm tin khi có bằng chứng xấu, và tính hợp lý của niềm tin. Nếu mô hình chỉ có các thành phần rời, việc hoán đổi chỉ làm đổi một câu trả lời.

**Nhóm cũng hỏi mô hình hình thành cách hiểu vào lúc nào.** Việc đặt bộ phân loại tại từ "believes" đã có trong `note.md` §2 *(phannhatminh đề xuất, note.md)*. Phần so sánh với vị trí cuối là phần thêm vào *(Claude đề xuất, phannhatminh chốt)*. Nếu bộ phân loại tại từ "believes" đã đọc được loại niềm tin, thì mô hình tự hình thành cách hiểu khi đọc câu, trước khi có câu hỏi nào. Nếu loại niềm tin chỉ xuất hiện ở vị trí cuối, sau câu hỏi, thì mô hình chỉ tính cách hiểu khi bị hỏi. Kết quả nào cũng đáng báo cáo.

**Câu hỏi chính thứ hai là giả thuyết thứ tư: khi AI hiểu lệch, lỗi nằm ở đâu?** *(huysuy05 đề xuất)* Khả năng thứ nhất là gộp ở mức biểu diễn, và khả năng thứ hai là gộp ở mức đọc ra, như đã mô tả ở mục 2. Theo kế hoạch của Huy, nếu bộ phân loại giải mã được cả xác suất được nêu lẫn việc có câu nói việc tin có ích tại những tầng mà câu đó đi vào câu trả lời, thì bằng chứng nghiêng về gộp ở mức đọc ra. Nếu DAS không tách được biến cách hiểu khỏi mức tin chắc được đọc ra, thì bằng chứng nghiêng về gộp ở mức biểu diễn. Thiết kế ba bên cho câu hỏi này thêm một đích đo cụ thể *(Claude đề xuất, phannhatminh chốt)*. Nhóm huấn luyện bộ phân loại để đọc mức tin chắc s mà người nói muốn truyền đạt từ trạng thái bên trong, rồi so con số đọc được với con số m mà mô hình trả lời. Nếu trạng thái bên trong chứa s rõ hơn câu trả lời m, thì lỗi nằm ở bước đọc ra. Nếu trạng thái bên trong không chứa s, thì lỗi nằm ở cách mô hình biểu diễn đoạn văn. Nhánh nghiên cứu trên người không làm được phép đo này, vì không thể nhìn vào trạng thái bên trong của người nghe.

**Đầu ra của phần định vị là một bản đồ theo tầng và theo vị trí từ, không phải một tầng duy nhất.** *(huysuy05 đề xuất)* Lý do là các hiệu ứng kiểu này thường trải qua nhiều tầng và nhiều đầu chú ý.

**Mô hình và hạ tầng.** *(huysuy05 đề xuất)* Phần cơ chế cần hai mô hình mở từ 7B trở lên, vì theo lời Huy, «Steele et al. [8] thấy khả năng theo dõi belief thất bại ở 3B». **[Claude sửa]** Claude cho rằng câu này đúng, và chỉ ghi thêm rằng bằng chứng đến từ bài thứ hai của Steele và cộng sự, không phải bài thứ nhất. Chi tiết ở mục 13, chỗ sửa thứ sáu. Mô hình thứ nhất là Qwen2.5-7B-Instruct, để nối tiếp pilot. Mô hình thứ hai là Llama-3.1-8B-Instruct, vì bản gốc của nó có SAE huấn luyện sẵn (Llama Scope, `note.md` §6.1). Cả hai chạy ở bf16 bằng PyTorch với nnsight hoặc pyvene, trên Colab Pro, hoặc trên NDIF nếu NDIF có host mô hình đó.

**Các phương pháp được chạy theo thứ tự từ rẻ đến đắt.** Thứ tự bốn phương pháp là của Huy *(huysuy05 đề xuất)*. Ý dùng bộ phân loại và việc ghép biểu diễn giữa các loại ngữ cảnh đã có trong `note.md` §2 *(phannhatminh đề xuất, note.md)*.

1. Phương pháp thứ nhất là logit lens. Nó theo dõi hiệu logit giữa Yes và No qua từng tầng, để thấy câu trả lời ở VD và IR tách nhau từ tầng nào.
2. Phương pháp thứ hai là ghép trạng thái bên trong giữa hai đoạn văn. Có hai cặp đoạn văn. Cặp thứ nhất gồm IR và VD, hai phiên bản chỉ khác nhau ở câu nói việc tin có ích, và việc ghép được làm tại các từ của câu đó, tại từ "believes" và tại từ cuối *(huysuy05 đề xuất)*. Mỗi lần ghép đo được bao nhiêu phần chênh lệch P(Yes) được khôi phục. Attribution patching được dùng để quét nhanh, ghép chính xác được dùng để xác nhận, rồi path patching thu hẹp kết quả xuống mức đầu chú ý *(huysuy05 đề xuất)*. Cặp thứ hai gồm VD-K và VD. Cặp này cho biết thông tin mức tin chắc cần được đưa vào đâu để câu trả lời trở nên đúng *(Claude đề xuất, phannhatminh chốt)*.
3. Phương pháp thứ ba huấn luyện các bộ phân loại tuyến tính ở từng tầng. Có bốn đích đọc. Đích thứ nhất là loại niềm tin *(phannhatminh đề xuất, note.md)*. Đích thứ hai là xác suất được nêu trong văn bản, và đích thứ ba là việc đoạn văn có câu nói việc tin có ích hay không *(huysuy05 đề xuất)*. Đích thứ tư là mức tin chắc s mà người nói muốn truyền đạt *(Claude đề xuất, phannhatminh chốt)*.
4. Phương pháp thứ tư là DAS. Nó tìm một không gian con hạng thấp mang mức tin chắc được gán tại các tầng đã định vị, rồi dùng phép hoán đổi để kiểm tra xem thay đổi biến cách hiểu có làm mức tin chắc được đọc ra thay đổi theo không *(huysuy05 đề xuất)*. Phép hoán đổi để phân biệt biến thống nhất với các thành phần rời được mô tả ở trên *(Claude đề xuất, phannhatminh chốt)*.

**Bộ phân loại phải được bảo vệ khỏi việc học tín hiệu bề mặt.** Biện pháp thứ nhất là so với mô hình túi từ chỉ dùng ngữ cảnh. Biện pháp thứ hai là kiểm tra trên những lĩnh vực mà bộ phân loại chưa gặp. Hai biện pháp này đã có trong `note.md` §2 và §3 *(phannhatminh đề xuất, note.md)*. Biện pháp thứ ba là dùng tác vụ kiểm soát theo Hewitt và Liang *(huysuy05 đề xuất)*.

**Quy trình được kiểm tra trên một cơ chế đã biết trước khi tìm cơ chế mới.** Nhóm chạy lại thí nghiệm phân biệt niềm tin với thực tế của Steele và cộng sự trên một mô hình 7B để làm đối chứng dương *(phannhatminh đề xuất, note.md)*.

**Với trạng thái hiện tại, phần cơ chế chỉ làm được việc chuẩn bị và thăm dò.** *(Claude đề xuất, phannhatminh chốt)* **[Khác kế hoạch của Huy]** Kế hoạch của Huy cho rằng nhánh cơ chế có thể bắt đầu từ tháng 11 trên 24 tình huống của pilot, trước khi có dữ liệu người, vì nhánh này hỏi mô hình tính ra câu trả lời như thế nào chứ không hỏi câu trả lời có đúng không. Tài liệu này đồng ý rằng công việc có thể bắt đầu từ tháng 11. Tuy vậy, có ba lý do khiến kết quả trên pilot chưa dùng được cho bài:

- Lý do thứ nhất là pilot chưa có dữ liệu người nói, nên chưa có nhãn cách hiểu từ người nói và chưa có đích s.
- Lý do thứ hai là yếu tố gây nhiễu mà Huy đã chỉ ra ở mục 4. Nếu định vị hiệu ứng trên các tình huống của pilot, nhóm có thể định vị một suy luận hợp lý chứ không phải một cách hiểu.
- Lý do thứ ba là mọi tình huống pilot đều nêu xác suất khách quan quanh mức một phần mười, nên bộ phân loại không có đủ độ biến thiên để học đọc mức tin chắc.

**[Cần thống nhất]** Hai người cần quyết định kết quả cơ chế trên pilot được dùng để báo cáo hay chỉ để kiểm tra công cụ.

Có năm việc cơ chế làm được ngay:

1. Việc thứ nhất là dựng hạ tầng ở bf16 bằng PyTorch *(huysuy05 đề xuất)* và kiểm tra kết quả khớp với bản 4-bit *(Claude đề xuất, phannhatminh chốt)*.
2. Việc thứ hai là chạy logit lens và ghép trạng thái trên pilot *(huysuy05 đề xuất)*.
3. Việc thứ ba là đặt bộ phân loại tại từ "believes" trên pilot để thăm dò xem ba phiên bản của mỗi tình huống có tách nhau trong biểu diễn không *(Claude đề xuất, phannhatminh chốt)*. Việc này làm được vì ba phiên bản dùng chung câu đích từng chữ.
4. Việc thứ tư là viết một bộ tình huống nhỏ riêng cho bộ phân loại, trong đó xác suất được nêu thay đổi từ thấp đến cao *(Claude đề xuất, phannhatminh chốt)*.
5. Việc thứ năm là chạy đối chứng dương theo công trình của Steele và cộng sự *(phannhatminh đề xuất, note.md)*.

## 8. Nếu có khoảng chênh, nhóm sửa mô hình bằng can thiệp tại vị trí đã định vị

Toàn bộ mục này là của Huy *(huysuy05 đề xuất)*, trừ những chỗ ghi nhãn khác.

**Ý tưởng thay một tầng của mô hình bằng BERT không chạy được như mô tả, vì ba lý do.**

- Lý do thứ nhất là BERT có bộ tách từ và không gian embedding riêng, với kích thước ẩn 768. Trong khi đó Qwen2.5-7B có kích thước ẩn 3.584, và Llama-3.1-8B có kích thước ẩn 4.096.
- Lý do thứ hai là mỗi tầng transformer tính rất nhiều đặc trưng không liên quan đến niềm tin, nên thay cả một tầng sẽ làm hỏng mô hình trên diện rộng.
- Lý do thứ ba là tầng nơi causal tracing định vị được hiệu ứng thường không phải tầng mà việc chỉnh sửa ở đó hiệu quả nhất (Hase và cộng sự 2023).

Dù vậy, cốt lõi của ý tưởng là hợp lý. Việc chèn một module nhỏ đã huấn luyện vào đúng vị trí đã định vị là việc đã có dạng chuẩn.

**Phương pháp chính là ReFT, cụ thể là LoReFT.** ReFT huấn luyện một can thiệp hạng thấp trên trạng thái ẩn tại các tầng và vị trí được chọn. Với hạng 4 trên dòng dư 4.096 chiều, mỗi vị trí chỉ cần khoảng 33 nghìn tham số. Can thiệp được huấn luyện trên mục tiêu lấy từ dữ liệu người ở một số lĩnh vực. Sau đó can thiệp được kiểm tra trên các lĩnh vực giữ lại, trên các tình huống bi quan phòng vệ, và trên hai bộ kiểm tra bên ngoài. Bortoletto và cộng sự (2025) đã sửa được các suy luận theory of mind sai bằng chỉnh sửa activation có mục tiêu, nên cách làm này đã có tiền lệ cho việc gán niềm tin. **[Cần thống nhất]** Theo thiết kế ba bên, cần quyết định mục tiêu huấn luyện lấy từ người nghe hay từ người nói.

**Có ba baseline.**

- Baseline thứ nhất là activation steering tại cùng các tầng (Rimsky và cộng sự 2024).
- Baseline thứ hai là LoRA, chạy ở ba bản. Bản thứ nhất giới hạn ở các tầng đã định vị, bản thứ hai chạy trên mọi tầng, và bản thứ ba chạy trên các tầng ngẫu nhiên. Phép so ba bản này biến nhận định về vị trí thành một phép thử.
- Baseline thứ ba là một câu lệnh yêu cầu mô hình tách mức tin chắc khỏi thái độ tin.

**BERT vẫn có hai vai trò.** Vai trò thứ nhất là một encoder nhỏ được tinh chỉnh để phân loại cách hiểu từ ngữ cảnh. Nó là baseline chỉ dùng văn bản, cho thấy thông tin có sẵn trong văn bản. Vai trò thứ hai là chính bộ phân loại đó có thể làm bộ định tuyến, chỉ bật steering ở ngữ cảnh thuộc cách hiểu thứ hai. Cách này cùng tinh thần với conditional activation steering (Lee và cộng sự 2025), vốn chỉ áp một vector steering khi đầu vào khớp một điều kiện.

**Transcoder là dạng hiện có gần nhất với ý "thay một tầng".** Transcoder là các bản thay thế thưa được huấn luyện cho tầng MLP. Nhưng transcoder được làm để diễn giải chứ không phải để sửa, và chỉ đáng dùng nếu đã có sẵn cho mô hình được chọn.

**Bất kỳ cách sửa nào cũng phải thỏa ba điều kiện.**

- Điều kiện thứ nhất là giữ nguyên mức tin chắc cao ở phiên bản TS.
- Điều kiện thứ hai là không làm giảm kết quả trên bài kiểm tra niềm tin sai thông thường (BigToM) và trên năng lực chung.
- Điều kiện thứ ba, theo bản của Huy, là cải thiện CI, SCE và HA trên dữ liệu giữ lại. **[Khác kế hoạch của Huy]** Theo thiết kế ba bên, điều kiện này thêm yêu cầu thu hẹp khoảng cách của AI so với ý người nói trên dữ liệu giữ lại *(phannhatminh đề xuất)*.

Nếu hai khoảng cách tương đương, phần cơ chế vẫn có giá trị. Câu hỏi chính thứ nhất ở mục 7 vẫn được trả lời đầy đủ, và câu hỏi chính thứ hai vẫn được trả lời trên những tình huống mà AI hiểu lệch.

## 9. Mốc quyết định, lịch, nơi nộp và ngân sách

**Mốc thứ nhất, vào cuối tháng 10.** *(huysuy05 đề xuất)* Theo kế hoạch của Huy, nhóm thu đường chuẩn từ 9 người nghe bằng biểu mẫu hiện có. Nếu người cũng nói rằng người tin theo cách hiểu thứ hai nghĩ điều họ tin có khả năng cao, thì cách đặt vấn đề "mô hình gộp niềm tin với mức tin chắc" phải đổi. Khi đó bài trở thành phép thử xem mô hình có tái tạo khuôn mẫu hiểu của người không, với cảm xúc là thao tác chính, và nửa sửa mô hình nhiều khả năng sẽ bị bỏ. **[Khác kế hoạch của Huy]** Theo thiết kế ba bên, nhóm thu thêm dữ liệu thử từ một nhóm nhỏ người nói *(phannhatminh đề xuất)*. Nhờ vậy mốc này phân biệt được hai cách giải thích *(Claude đề xuất, phannhatminh chốt)*. Nếu người nói cũng muốn truyền đạt mức tin chắc cao, thì khung lý thuyết cần sửa. Nếu người nói muốn truyền đạt mức tin chắc thấp mà người nghe hiểu thành cao, thì đó là một khoảng hở thật trong giao tiếp giữa người với người.

**Mốc thứ hai, vào giữa tháng 2.** *(huysuy05 đề xuất)* Theo kế hoạch của Huy, nhóm xem dữ liệu người đầy đủ và kết quả chạy mô hình có cho thấy khoảng chênh giữa mô hình và người ở CI hoặc SCE hay không. Nếu có, nhóm làm mục 8. Nếu không, bài báo cáo mức khớp cùng cách mô hình tính mức tin chắc được gán. **[Khác kế hoạch của Huy]** Theo thiết kế ba bên, tiêu chí là khoảng cách của AI có lớn hơn rõ rệt so với khoảng cách của người nghe là người hay không *(phannhatminh đề xuất)*. **[Cần thống nhất]** Tiêu chí này phụ thuộc vào quyết định về chỉ số trung tâm ở mục 5.

**Mốc thứ ba, vào giữa tháng 3.** *(huysuy05 đề xuất)* Nhóm chọn nơi nộp theo những gì đã sẵn sàng.

**Lịch theo tháng.** *(huysuy05 đề xuất)* Nhánh A là bộ đánh giá và nghiên cứu trên người. Nhánh B là phần cơ chế.

- Trong tháng 10, nhánh A làm Mốc 1, nộp IRB, tải tình huống từ OSF và chạy mô hình trên hai nghiên cứu đã công bố. Nhánh B chạy lại pilot ở bf16 bằng PyTorch.
- Trong tháng 11, nhánh A viết và kiểm định bộ tình huống bản 2, và mở rộng hệ thống chạy mô hình cho mức tin chắc dạng số, thước đo đặc trưng và mô hình API. Nhánh B chạy logit lens và ghép trạng thái trên tình huống của pilot.
- Trong tháng 12 và tháng 1, nhánh A thu dữ liệu người trên Prolific và chạy toàn bộ mô hình. Nhánh B huấn luyện bộ phân loại và ghép trạng thái trên bộ tình huống bản 2.
- Trong tháng 2, nhánh A phân tích dữ liệu và làm Mốc 2. Nhánh B chạy DAS.
- Trong tháng 3, nhánh A làm Mốc 3 và các thí nghiệm loại bỏ thành phần. Nhánh B làm ReFT, steering và LoRA theo tầng đã định vị, nếu có khoảng chênh.
- Trong tháng 4, cả hai nhánh viết bài. Nhánh A thêm dataset card và công bố dữ liệu.
- Trong tháng 5, nhóm nộp bài.

Nếu có hai người, mỗi người phụ trách một nhánh là cách chia tự nhiên. **[Cần thống nhất]** Hai người chưa quyết định ai phụ trách nhánh nào. Nhóm người nói ở thiết kế ba bên thêm việc cho nhánh A trong tháng 10 và trong tháng 12 đến tháng 1.

**Nơi nộp.** *(huysuy05 đề xuất)* Lịch năm 2027 chưa được công bố, nên các hạn dưới đây lấy theo năm 2026 và đã được kiểm chứng trên trang chính thức.

- Nhánh Evaluations & Datasets của NeurIPS có hạn phần tóm tắt ngày 4/5 và hạn bài ngày 6/5. Nhánh này hợp với một bài đặt bộ đánh giá lên trước. Nó nhận bộ đánh giá mới, phương pháp đánh giá, nghiên cứu lấy con người làm trung tâm và kết quả âm. Nó yêu cầu host dữ liệu trên một nền tảng như Hugging Face, kèm siêu dữ liệu Croissant.
- Chu kỳ tháng 5 của ACL Rolling Review có hạn ngày 25/5, cho EMNLP hoặc AACL. Chu kỳ này hợp với một bài đặt phát hiện lên trước, viết cho cộng đồng NLP và ngôn ngữ học.
- Workshop về diễn giải cơ chế tại ICML có hạn ngày 8/5. Workshop này hợp với phần định vị và sửa mô hình. Nó không lưu trữ chính thức, nhận bài 4 hoặc 8 trang, và nhận cả bài đang được NeurIPS phản biện.
- CogSci có hạn ngày 2/2. Hội nghị này chỉ hợp với phiên bản thuần khoa học xã hội.

Hướng đề xuất là nộp nhánh Evaluations & Datasets của NeurIPS nếu Mốc 2 thuận lợi, đồng thời gửi phần cơ chế tới workshop tại ICML. Nếu bài chưa kịp hạn đầu tháng 5, chu kỳ tháng 5 của ACL Rolling Review muộn hơn khoảng ba tuần.

**Ngân sách.** *(huysuy05 đề xuất)* Dữ liệu người nghe tốn khoảng 760 đô la. Chạy API tốn từ 30 đến 100 đô la. GPU tốn từ 75 đến 150 đô la. Tổng cộng khoảng từ 870 đến 1.010 đô la, gần mức thấp của ước tính giai đoạn 1 trong `note.md` (từ 900 đến 1.500 đô la). **[Khác kế hoạch của Huy]** Con số này chưa gồm nhóm người nói, vì kích thước nhóm đó chưa được ước tính.

## 10. Trong hai tuần tới có các việc cụ thể sau

1. *(phannhatminh đề xuất)* Thiết kế biểu mẫu cho người nói, trong đó sự thật về nhân vật được viết bằng ngôn ngữ không chứa chữ "believe".
2. *(huysuy05 đề xuất)* Thu đường chuẩn từ 9 người nghe bằng biểu mẫu hiện có, và coi đây là kiểm tra nội bộ. Theo thiết kế ba bên, thu thêm dữ liệu thử từ một nhóm nhỏ người nói *(phannhatminh đề xuất)*.
3. *(huysuy05 đề xuất)* Nộp hồ sơ IRB cho nghiên cứu đầy đủ, bao gồm cả hai nhóm người tham gia.
4. *(huysuy05 đề xuất)* Tải tình huống từ OSF của Vesga và của Cusimano, rồi chạy các mô hình của pilot trên đó bằng `pilot/run.py`.
5. *(huysuy05 đề xuất)* Viết lại `pilot/stimuli.py` theo tám phiên bản và theo hai loại câu nói việc tin có ích.
6. *(huysuy05 đề xuất)* Chạy lại pilot Qwen2.5-7B ở bf16 bằng PyTorch, và làm lượt ghép trạng thái đầu tiên theo tầng và vị trí.
7. *(Claude đề xuất, phannhatminh chốt)* Đặt bộ phân loại tại từ "believes" trên pilot để thăm dò, và viết bộ tình huống nhỏ có xác suất được nêu thay đổi cho bộ phân loại.
8. *(huysuy05 đề xuất)* Cập nhật `README.md` và `note.md` §0, §8 theo phạm vi mới.

## 11. Bản nháp abstract

Bản nháp này là của Huy *(huysuy05 đề xuất)*. Nó được giữ bằng tiếng Anh vì sẽ dùng trực tiếp trong bài. **[Khác kế hoạch của Huy]** Bản nháp được viết trước khi có thiết kế ba bên, nên chưa nhắc đến người nói. **[Cần thống nhất]** Hai người cần viết lại abstract sau khi chốt chỉ số trung tâm ở mục 5.

> Evaluations of belief attribution in language models almost always use beliefs that track evidence. The verb "believe" also reports value-driven belief. A patient told that her surgery succeeds one time in ten may believe it will succeed because patients who believe recover better, while her credence stays low. Holding the sentence "X believes that p" fixed and varying only its context, we ask whether models attribute to X the credence and belief profile that human readers do. We introduce [NAME], a benchmark of [N] items crossing evidence, the practical stake of believing, the believer's emotion and an explicitly stated credence, normed by [N] human raters, with human-relative metrics for credence inflation, stated-credence error and alignment. Across [K] models, [finding]. We also replicate two published human studies of belief attribution with models, and we localize the attribution of credence in [models] with activation patching and distributed alignment search. Finally, we [show that a low-rank intervention at the localized layers closes the gap / characterize the mechanism].

## 12. Danh sách các chỗ cần thống nhất giữa phannhatminh và huysuy05

1. Giả thuyết thứ nhất theo bản của Huy hay theo bản ba bên (mục 2).
2. Thước đo đặc trưng của Vesga dùng cho AI như kế hoạch của Huy, hay chỉ dùng cho người nói là người (mục 5).
3. Chỉ số trung tâm của bài là CI của Huy, hay hiệu giữa hai khoảng cách của thiết kế ba bên (mục 5).
4. Người nói có dùng cùng 8 danh sách Latin square với người nghe không, và mỗi ô cần bao nhiêu người nói (mục 6).
5. Kết quả cơ chế trên pilot được dùng để báo cáo hay chỉ để kiểm tra công cụ (mục 7).
6. Mục tiêu huấn luyện ReFT lấy từ người nghe hay từ người nói (mục 8).
7. Tiêu chí của Mốc 2 (mục 9).
8. Ai phụ trách nhánh A và ai phụ trách nhánh B (mục 9).
9. Viết lại abstract theo thiết kế ba bên (mục 11).
10. Huy xem lại sáu chỗ Claude sửa hoặc làm rõ kế hoạch của Huy, và xác nhận hoặc bác từng chỗ (mục 13).

## 13. Các chỗ Claude sửa hoặc làm rõ kế hoạch của Huy

Mục này liệt kê mọi chỗ mà tài liệu này thay đổi lời của Huy vì lý do dữ kiện, chứ không phải vì thiết kế ba bên. Các thay đổi về thiết kế được đánh dấu riêng bằng **[Khác kế hoạch của Huy]** và không nằm trong mục này. Mọi bằng chứng dưới đây đến từ việc Claude đọc toàn văn các bài gốc và đếm lại dữ liệu vào ngày 27/9/2026. Trong bản `direction.md` trước, sáu chỗ này bị viết lại mà không giữ lời gốc của Huy; bản này khôi phục lời gốc và nêu rõ từng thay đổi. Mỗi chỗ đều cần Huy xem lại.

**Chỗ sửa thứ nhất là mô tả bài của Yongsatianchot và Marsella (WishfulEval), ở mục 2.**

- Huy viết rằng bài này thấy wishful thinking trong ước lượng xác suất của chính mô hình, và hiện tượng xuất hiện chủ yếu khi prompt có câu "You feel really hopeful about the outcome.".
- Claude cho rằng vế thứ nhất sai. Bài có ba điều kiện nhập vai: không nhập vai, nhập vai trực tiếp, và nhập vai một nhân vật cụ thể. Ước lượng ở điều kiện không nhập vai giữ ở mức nền, nên bài không cho thấy wishful thinking trong ước lượng của chính mô hình. Thiên lệch chỉ xuất hiện khi mô hình nhập vai một nhân vật. Câu "hopeful" cũng thuộc một điều kiện nhập vai, là điều kiện nhân vật có chỉ dẫn và trạng thái hy vọng trong Thí nghiệm 2.
- Claude cho rằng vế thứ hai phóng đại vai trò của câu "hopeful". Trong Thí nghiệm 1, hai mô hình đã có thiên lệch ở các miền thể thao khi nhập vai, mà không cần câu đó. Câu "hopeful" chỉ cần thiết để tạo thiên lệch ở miền bài toán logic, tức miền rút bi từ bình.
- Claude sửa thành: wishful thinking trong bài chỉ xuất hiện khi mô hình nhập vai một nhân vật, và câu "hopeful" chỉ cần thiết ở miền bài toán logic.
- Hệ quả của lỗi này là đề xuất so sánh ngôi thứ nhất của Huy ở mục 6 mất cơ sở, vì bài không có dữ liệu wishful thinking ở ngôi thứ nhất.
- Nguồn là bài "Investigating Motivated Inference in Large Language Models", WiNLP 2025, phần tóm tắt, mục Thí nghiệm 1 và mục Thí nghiệm 2.

**Chỗ sửa thứ hai là chức năng của niềm tin trong các tình huống của Vesga và cộng sự, ở mục 6.**

- Huy viết rằng niềm tin không nhằm vào sự thật trong bài này phục vụ bản sắc, lòng trung thành và điều hòa cảm xúc.
- Claude cho rằng danh sách này không khớp với các tình huống thật của bài. Bài dùng bốn cặp tình huống. Cặp thứ nhất về lòng trung thành với một người bạn. Cặp thứ hai về đức tin tôn giáo. Cặp thứ ba về cam kết đạo đức của một giáo viên muốn nhìn thấy tiềm năng của học sinh, lấy ý từ Cusimano và Lombrozo. Cặp thứ tư về bản sắc và mong muốn sống thật với bản thân. Điều hòa cảm xúc chỉ được nêu trong phần tóm tắt như một ví dụ chung về chức năng của niềm tin, và không có tình huống nào dành cho nó. Danh sách của Huy vì vậy thiếu đức tin tôn giáo và cam kết đạo đức, và có một chức năng không được thao tác trong thí nghiệm.
- Claude sửa danh sách thành lòng trung thành, đức tin tôn giáo, cam kết đạo đức và bản sắc.
- Kết luận của Huy không bị ảnh hưởng, vì không tình huống nào trong bốn cặp có cấu trúc "tin để kết cục tốt hơn".
- Nguồn là bài "Evidence for multiple kinds of belief in theory of mind", Journal of Experimental Psychology: General 2025, phần mô tả tình huống của Nghiên cứu 1.

**Chỗ sửa thứ ba là số người trong các nghiên cứu của Cusimano và Lombrozo, ở mục 6.**

- Huy viết rằng các nghiên cứu của họ có N = 839 và 1.021.
- Claude cho rằng con số này thiếu một nghiên cứu. Bài có ba nghiên cứu. Nghiên cứu 1 có 839 người, Nghiên cứu 2 có 1.021 người, và Nghiên cứu 3 có 233 người. Cả ba con số là mẫu phân tích, sau khi đã loại những người trượt câu kiểm tra thông hiểu.
- Claude bổ sung Nghiên cứu 3 với 233 người.
- Thiếu sót này không làm thay đổi lập luận của Huy.
- Nguồn là bài "Morality justifies motivated reasoning in the folk ethics of belief", Cognition 2021, các mục 2.1.1, 3.1.1 và 4.1.1.

**Chỗ sửa thứ tư là cách mô tả thiết kế của WishfulEval, ở mục 6.**

- Huy viết rằng bộ này kết hợp mức mong muốn kết cục với độ mạnh của bằng chứng trong các bài ước lượng xác suất.
- Claude không cho rằng câu này sai. Bài gốc gọi biến thứ hai là độ bất định của thông tin, và thao tác nó bằng mức xác suất nền cùng số lần mô phỏng được cho mô hình xem. Cách gọi "độ mạnh của bằng chứng" của Huy là một cách diễn đạt gần đúng cho biến này.
- Trong bản `direction.md` trước, Claude đã thay lời của Huy bằng "độ chắc chắn của thông tin" mà không ghi chú. Bản này khôi phục lời của Huy và chỉ ghi thêm thuật ngữ của bài gốc.
- Nguồn là bài WiNLP 2025 đã nêu ở chỗ sửa thứ nhất, mục phương pháp của Thí nghiệm 1.

**Chỗ sửa thứ năm là số bình luận GoEmotions có khung chủ ý, ở mục 6.**

- Huy viết rằng chỉ 15 bình luận dùng khung chủ ý như "choose to", "need to" hoặc "want to believe".
- Claude tải ba tệp train, dev và test của GoEmotions từ kho google-research, tổng cộng 54.263 bình luận, và đếm lại. Con số 457 bình luận có một dạng của động từ "believe" khớp chính xác với con số của Huy. Với ba khung "choose to", "need to" và "want to" đứng trước "believe", kể cả các dạng chia thì, Claude đếm được 11 bình luận. Khi nới thêm các khung "decide to", "try to", "refuse to" và "like to", con số là 16. Không có cách đếm nào Claude thử ra đúng 15.
- Claude không khẳng định Huy sai, vì Huy có thể đã dùng một danh sách khung khác. Claude ghi cả hai con số.
- Kết luận của Huy không đổi: số bình luận có khung chủ ý quá ít để dùng làm dữ liệu.

**Chỗ sửa thứ sáu là lý do cần mô hình từ 7B trở lên, ở mục 7.**

- Huy viết rằng Steele và cộng sự thấy khả năng theo dõi niềm tin thất bại ở 3B.
- Claude cho rằng câu này đúng. Bài thứ hai của Steele và cộng sự (arXiv 2607.11945) viết rằng khả năng gán niềm tin xuất hiện đột ngột trong khoảng từ 3B đến 7B trên năm họ mô hình, và ba mô hình 3B đều thất bại ở phép thử của họ.
- Claude chỉ ghi thêm rằng bằng chứng này đến từ bài thứ hai. Bài thứ nhất (arXiv 2607.10248) lại dùng chính Qwen2.5-3B làm mô hình chính cho cơ chế định tuyến của nó. Vì vậy nếu có người phản biện rằng mô hình 3B vẫn dùng được, nhóm cần dẫn đúng bài thứ hai.
- Trong bản `direction.md` trước, Claude đã viết lại câu của Huy thành "khả năng theo dõi niềm tin chỉ xuất hiện trong khoảng từ 3B đến 7B" mà không ghi chú. Bản này khôi phục lời của Huy.

## Tài liệu tham khảo

Danh sách này lấy từ `revised_plan_believe.md` *(huysuy05 đề xuất)*.

1. Kunda, Z. (1990). The case for motivated reasoning. Psychological Bulletin, 108(3), 480-498.
2. Lerner, J. S., and Keltner, D. (2001). Fear, anger, and risk. Journal of Personality and Social Psychology, 81(1), 146-159.
3. Krizan, Z., and Windschitl, P. D. (2007). The influence of outcome desirability on optimism. Psychological Bulletin, 133(1), 95-121.
4. Vesga, A., Van Leeuwen, N., and Lombrozo, T. (2025). Evidence for multiple kinds of belief in theory of mind. Journal of Experimental Psychology: General. OSF project 38YGN.
5. Yongsatianchot, N., and Marsella, S. (2025). Investigating motivated inference in large language models. Proceedings of the 9th Widening NLP Workshop (WiNLP). Code: WishfulEval.
6. Norem, J. K., and Cantor, N. (1986). Defensive pessimism: Harnessing anxiety as motivation. Journal of Personality and Social Psychology, 51(6), 1208-1217.
7. Cusimano, C., and Lombrozo, T. (2021). Morality justifies motivated reasoning in the folk ethics of belief. Cognition, 209, 104513.
8. Steele, Wen, and Han (2026). One mechanism for many mental spaces, arXiv 2607.10248; và Belief-reality separation lives in routing, arXiv 2607.11945. Corpus và code: osteele/mental-spaces.
9. Demszky, D., et al. (2020). GoEmotions: A dataset of fine-grained emotions. ACL 2020.
10. de Marneffe, M.-C., Simons, M., and Tonhauser, J. (2019). The CommitmentBank: Investigating projection in naturally occurring discourse. Sinn und Bedeutung 23.
11. Rashkin, H., Smith, E. M., Li, M., and Boureau, Y.-L. (2019). Towards empathetic open-domain conversation models: A new benchmark and dataset. ACL 2019.
12. Meng, K., Bau, D., Andonian, A., and Belinkov, Y. (2022). Locating and editing factual associations in GPT. NeurIPS 2022.
13. Syed, A., Rager, C., and Conmy, A. (2023). Attribution patching outperforms automated circuit discovery. arXiv 2310.10348.
14. Hewitt, J., and Liang, P. (2019). Designing and interpreting probes with control tasks. EMNLP 2019.
15. Geiger, A., Wu, Z., Potts, C., Icard, T., and Goodman, N. (2024). Finding alignments between interpretable causal variables and distributed neural representations. CLeaR 2024.
16. Hase, P., Bansal, M., Kim, B., and Ghandeharioun, A. (2023). Does localization inform editing? Surprising differences in causality-based localization vs. knowledge editing in language models. NeurIPS 2023.
17. Wu, Z., Arora, A., Wang, Z., Geiger, A., Jurafsky, D., Manning, C. D., and Potts, C. (2024). ReFT: Representation finetuning for language models. NeurIPS 2024.
18. Bortoletto, M., et al. (2025). Brittle minds, fixable activations: Understanding belief representations in language models. Findings of EMNLP 2025; arXiv 2406.17513.
19. Rimsky, N., et al. (2024). Steering Llama 2 via contrastive activation addition. ACL 2024.
20. Lee, B. W., et al. (2025). Programming refusal with conditional activation steering. ICLR 2025; arXiv 2409.05907.
21. Dunefsky, J., Chlenski, P., and Nanda, N. (2024). Transcoders find interpretable LLM feature circuits. NeurIPS 2024.
22. Gandhi, K., Fränken, J.-P., Gerstenberg, T., and Goodman, N. D. (2023). Understanding social reasoning in language models with language models. NeurIPS 2023, Datasets and Benchmarks track.
23. Trang lịch NeurIPS 2026 và call for papers của nhánh Evaluations & Datasets; trang lịch ACL Rolling Review; call for papers của workshop Mechanistic Interpretability tại ICML 2026; trang hội nghị CogSci 2026. Tất cả được truy cập ngày 27/9/2026.
