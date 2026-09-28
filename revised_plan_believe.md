# Kế hoạch sửa đổi: hai cách đọc chữ "believe" trong LLM

Mục tiêu: nộp bài khoảng tháng 5/2027. Viết dựa trên repo tại commit 087eba4 (README.md, note.md, pilot/), ngày 27/9/2026.

## 1. Những gì thay đổi

Câu hỏi nghiên cứu vẫn là đề bài đã chốt ở note.md §0. Khi câu "X believes that p" giữ nguyên từng chữ và chỉ ngữ cảnh thay đổi, mô hình ngôn ngữ có phân biệt được niềm tin truth-seeking với niềm tin vì giá trị không? Có năm thay đổi:

1. **Bài chuyển thành một benchmark có chuẩn từ người, nửa sau là phần mechanistic.** Cách này bao được cả hướng benchmark lẫn hướng khoa học xã hội. Đáp án đúng ở các item then chốt còn tranh cãi, nên đáp án tham chiếu buộc phải là phán đoán của người. Việc thu các phán đoán đó chính là nghiên cứu khoa học xã hội.
2. **Cảm xúc trở thành một biến được thao tác.** Biến này đồng thời là công cụ tách niềm tin vì giá trị (credence vẫn thấp) khỏi wishful thinking (credence tăng lên). note.md §7 đã nêu phân biệt này, nhưng pilot chưa kiểm tra được.
3. **Hai nghiên cứu trên người đã công bố trở thành bộ test bên ngoài.** Cả hai đều công khai stimuli và dữ liệu.
4. **Stimuli được sửa hai chỗ.** Một là confound trong cách câu stake vận hành. Hai là stimuli chưa nêu credence của chính người tin.
5. **Ý tưởng thay một layer trở thành quy trình hai bước.** Định vị hiệu ứng trước, rồi can thiệp tại đúng vị trí đó (§7, §8).

Ba phần sau chuyển sang hướng làm sau, vì không kịp trước tháng 5: ngôn ngữ hình thức belief / acceptance, belief-in, và mẫu tự nhiên lấy từ corpus (note.md A1 đến A4 và phần lớn §8).

## 2. Pilot cho thấy gì và chưa cho thấy được gì

Cả hai mô hình Qwen coi niềm tin vì giá trị là bền trước bằng chứng, và hợp lý hơn niềm tin đi ngược bằng chứng. Nhưng chúng vẫn gán credence cao cho người tin. P(thinks it is likely) là 0.71 ở VD so với 0.27 ở IR với Qwen2.5-7B, và 1.00 so với 0.80 với Qwen3-4B. Các đối chứng ở note.md §9.1 đã loại trừ chữ "convinced" và độ dài câu. Tuy vậy, ba đặc điểm của stimuli giới hạn ý nghĩa của kết quả này.

**Thứ nhất, câu stake thường làm thay đổi chính xác suất của p.** Theo cách tôi đọc, ở 21 trên 24 item, câu stake nói rằng việc tin làm tăng khả năng p xảy ra. Có khi là trực tiếp (Kenji đánh tốt hơn, Hana gọi vốn thuyết phục hơn), có khi là thông qua nỗ lực (Amara tiếp tục tìm kiếm, Farid tiếp tục tưới nước). Người đọc hiểu câu đó theo nghĩa đen thì nên đánh giá cơ hội của người tin cao hơn tỷ lệ nền. Vì vậy, một phần credence cao mà mô hình gán có thể là suy luận đúng, chứ không phải collapse.

Chỉ Maya, Leila và Ingrid có câu stake cải thiện một kết cục khác: hồi phục sau mổ, giữ được điều kiện nhận tim, và vượt qua giai đoạn căng thẳng. Đây mới đúng cấu trúc của phần formalize ở note.md §1, nơi việc tin thay đổi P(sống | thành công) chứ không thay đổi P(thành công).

Chia kết quả hiện có của Qwen2.5-7B theo hai nhóm này:
- Mức dịch chuyển credence VD trừ IR là +0.48 trên 21 item, và +0.20 trên 3 item.
- Credence trung bình ở VD là 0.76 so với 0.36.

Ba item không đủ để kết luận, nhưng chênh lệch đi đúng chiều mà confound dự đoán. Qwen3-4B chạm trần (1.00) ở cả hai nhóm.

**Thứ hai, credence của chính người tin chưa bao giờ được nêu.** Các đoạn văn chỉ nêu xác suất khách quan ("succeeds in only about one case out of ten"). Trong khi đó, note.md §3 đặt việc credence thấp được nêu rõ làm một phần tiêu chí vận hành cho cách đọc vì giá trị. Vì vậy câu "Does Maya think it is likely?" mơ hồ giữa thái độ cô ấy tuyên bố và credence thật bên dưới. Trả lời "yes" vẫn bảo vệ được nếu đọc theo nghĩa wishful thinking.

**Thứ ba, cảm xúc chưa được thao tác.** Các item chỉ khác nhau về sức nặng cảm xúc do chủ đề (bố hôn mê, một trận cờ vua), nên cảm xúc bị lẫn với miền.

Các giới hạn đã liệt kê ở note.md §9 vẫn còn nguyên:
- chưa có đường chuẩn người;
- mỗi câu hỏi chỉ có một cách diễn đạt;
- chỉ trả lời Yes/No;
- mô hình instruct lượng tử hóa 4-bit;
- n = 24.

## 3. Các cách đọc và giả thuyết

Bản sửa tách ba cách đọc của cùng một câu đích:

| Cách đọc | Điều gì dẫn dắt niềm tin | Credence |
|---|---|---|
| Truth-seeking (TS) | bằng chứng | cao |
| Vì giá trị (VD) | việc giữ niềm tin có ích | giữ ở mức xác suất được nêu |
| Có động cơ / wishful (MR) | mong muốn hoặc cảm xúc [1] | bị mong muốn hoặc cảm xúc kéo lệch |

Kết quả collapse của pilot tương đương với nhận định rằng mô hình đọc ngữ cảnh VD thành MR.

Giả thuyết về cảm xúc khớp vào đúng chỗ này, vì cảm xúc là đòn bẩy tự nhiên giữa VD và MR. Bằng chứng hiện có:
- Ở người, sợ hãi khiến phán đoán rủi ro bi quan hơn, còn tức giận khiến nó lạc quan hơn [2].
- Mong muốn một kết cục làm tăng khả năng người ta dự đoán kết cục đó xảy ra [3].
- Vesga et al. [4] xếp điều hòa cảm xúc vào các chức năng của niềm tin non-epistemic.
- Ở mô hình, Yongsatianchot và Marsella [5] thấy wishful thinking trong ước lượng xác suất của chính mô hình. Hiện tượng này xuất hiện chủ yếu khi prompt có câu "You feel really hopeful about the outcome."

**H1 (thổi phồng credence).** So với người đọc, mô hình gán credence cao hơn cho người tin kiểu VD. Điều này rõ nhất khi lợi ích rơi vào một kết cục khác p, hoặc khi credence thấp của người tin được nêu rõ.

**H2 (cảm xúc).** Với người đọc, "believes" đứng sau một câu sợ hãi sẽ được đọc theo nghĩa vì giá trị (credence vẫn thấp). Đứng sau một câu hy vọng, nó được đọc theo nghĩa wishful (credence tăng). Còn mô hình thì bám theo sắc thái tích cực hay tiêu cực của từ chỉ cảm xúc (hy vọng thì tăng, sợ hãi thì giảm), bất kể có stake hay không. Vì vậy hiệu ứng cảm xúc ở mô hình và ở người sẽ lệch nhau tại các ô có stake.

**H3 (sắc thái so với chức năng).** Trong các item bi quan phòng vệ (defensive pessimism), niềm tin có ích lại là một niềm tin không mong muốn. Ví dụ: một sinh viên tin rằng mình sẽ trượt để tiếp tục ôn bài [6]. Mô hình nào đồng nhất "tin" với "hy vọng" sẽ gán sai credence ở các item này, còn người thì không.

**H4 (cơ chế).** Có hai khả năng:
- **Gộp ở mức biểu diễn (representational collapse):** mạng không có một biến tách riêng cho credence của người tin.
- **Gộp ở mức đọc ra (readout collapse):** mạng có mã hóa xác suất được nêu, nhưng câu trả lời cho "thinks it is likely" lại bị câu tường thuật belief chi phối.

§7 được thiết kế để phân biệt hai khả năng này.

## 4. Thiết kế benchmark

Mỗi item gồm phần setup, mệnh đề p, bằng chứng mạnh hoặc yếu, một câu stake, một câu cảm xúc và một câu credence. Câu đích giữ nguyên qua mọi điều kiện.

Câu stake của mỗi item thuộc một trong hai loại:
- **Loại gián tiếp (downstream):** việc tin cải thiện một kết cục khác p, như việc hồi phục của Maya.
- **Loại tự hiện thực hóa (self-fulfilling):** việc tin làm tăng xác suất của chính p. Các item loại này nêu thêm xác suất trong nhóm người tin ("even fighters who go in convinced win only about one time in ten from his position").

Câu cảm xúc chỉ gọi tên một cảm xúc và không nói gì về xác suất ("Maya feels hopeful." hoặc "Maya feels frightened."). Câu credence tường thuật ước lượng của chính người tin ("Asked to put a number on it, Maya says her chances are about one in ten.").

Có tám điều kiện:

| Mã | Bằng chứng | Stake | Cảm xúc | Nêu credence của người tin | Vai trò |
|---|---|---|---|---|---|
| TS | mạnh | không | không | không | mốc neo |
| IR | yếu | không | không | không | tin ngược bằng chứng |
| IR-H | yếu | không | hy vọng | không | wishful thinking |
| IR-F | yếu | không | sợ hãi | không | cảm xúc không kèm stake |
| VD | yếu | có | không | không | điều kiện của pilot |
| VD-H | yếu | có | hy vọng | không | H2 |
| VD-F | yếu | có | sợ hãi | không | H2 |
| VD-K | yếu | có | không | có | H1, phép thử sạch nhất |

Bộ lõi gồm 96 item trên 8 miền, một nửa loại gián tiếp và một nửa loại tự hiện thực hóa. Thêm vào đó là 24 item bi quan phòng vệ ở các điều kiện TS, IR, VD và VD-K.

24 item của pilot, sau khi viết lại, trở thành bộ phát triển (dev set) cùng với hai đối chứng từ vựng VDn và IRf. Pilot §9.1 đã cho thấy thêm một câu trung tính không làm credence tăng. Vì vậy hai đối chứng này không cần thu chuẩn người ở quy mô đầy đủ. Có thể dùng LLM viết nháp từ template, với hai điều kiện: cả hai tác giả sửa từng item, và có một vòng kiểm định nhỏ trước khi thu chuẩn.

**Câu hỏi và thước đo.** Ba câu hỏi của pilot được giữ lại, mỗi câu có hai cách diễn đạt. Thêm ba loại thước đo:
- **Credence dạng số** ("What chance does Maya think the surgery has, from 0 to 100?"). Đây là thước đo liên tục, và dùng được cho các mô hình API không trả log-probability.
- **Một câu phân loại tường minh** ("Does Maya hold this belief mainly because of the evidence, or mainly because believing helps her?"). Câu này cho biết mô hình có gọi tên được cách đọc hay không.
- **Hai thước đo signature của Vesga et al. [4],** đọc từ log-probability tại vị trí động từ: "thinks" so với "believes", và "decided to believe" so với "decided whether to believe". Người ta ưu tiên "thinks" và "decided whether" cho niềm tin epistemic. Vì hai thước đo này không cần câu hỏi, có thể chấm cả mô hình base lẫn mô hình instruct.

**Thu chuẩn người.** Dùng Latin square trên 8 danh sách, mỗi người đọc 24 đoạn (khoảng 15 phút). Với ít nhất 5 đánh giá cho mỗi ô item × điều kiện, cần $96 \times 8 \times 5 / 24 = 160$ người. Sau khi loại 15%, con số là khoảng 190 người. Theo mức $16 mỗi giờ-người trong note, tổng khoảng $760. Nên pre-register thiết kế, tiêu chí loại và các phép so sánh chính. pilot/build_form.py và template của form có thể mở rộng cho việc này bằng cách thêm danh sách.

**Bộ mô hình.**
- Các cặp base và instruct ở hai hoặc ba kích cỡ, từ hai hoặc ba họ mô hình mở, ví dụ Qwen, Llama và OLMo. Dữ liệu huấn luyện mở của OLMo giúp trả lời câu hỏi về nhiễm dữ liệu.
- Ít nhất một mô hình chạy thêm ở bf16 để kiểm tra lại kết quả 4-bit.
- Hai đến bốn mô hình API, chấm qua câu trả lời dạng số và lấy mẫu.

## 5. Dữ liệu có sẵn

**Vesga, Van Leeuwen và Lombrozo [4].** Ba nghiên cứu đã pre-register (N = 383, 723 và 740) về cách người gán niềm tin epistemic và non-epistemic, dùng các signature ở trên. Stimuli, dữ liệu và script phân tích đều có trên OSF (project 38YGN). Có thể cho mô hình làm người tham gia trên đúng các vignette gốc, rồi so với kết quả đã công bố. Lưu ý: niềm tin non-epistemic của họ phục vụ bản sắc, lòng trung thành và điều hòa cảm xúc, chứ không nhằm một kết cục tốt hơn. note.md §7 đã ghi điểm lệch này. Vì vậy đây là bộ test chuyển giao, không phải bộ lõi.

**Cusimano và Lombrozo [7].** Họ đặt bằng chứng đối lập với lợi ích đạo đức hoặc thực tiễn của việc tin. Một tình huống của họ có đúng cấu trúc VD loại gián tiếp: người chồng bị ung thư, tỷ lệ sống qua một năm là 15%, và sự lạc quan giúp cả gia đình sống tốt hơn. Các nghiên cứu của họ (N = 839 và 1.021) đo niềm tin mà người ta cho là nhân vật nên có, so với khoảng mà bằng chứng cho phép. Họ cũng đo các phán đoán về tính chính đáng và về tri thức. Stimuli và dữ liệu có trên OSF. Đây là bộ test bên ngoài thứ hai, và là dữ liệu người đã công bố gần nhất với khái niệm VD.

**WishfulEval [5].** Bộ này kết hợp mức mong muốn kết cục với độ mạnh của bằng chứng trong các bài ước lượng xác suất, và có sẵn thao tác "hopeful". Code công khai. Bộ này cho một template cho biến cảm xúc, và một phép so sánh ngôi thứ nhất: wishful thinking của chính mô hình có dự đoán được điều nó gán cho người khác không?

Các vignette đã công bố của [4], [5] và [7] có thể nằm trong dữ liệu huấn luyện. Vì vậy mỗi bản gốc cần chạy song song với một bản diễn đạt lại.

**Mental-spaces của Steele, Wen và Han [8]** (note.md §7). Corpus và code này làm đối chứng dương cho phần mechanistic (belief so với reality).

**Ba corpus trông hứa hẹn nhưng không phù hợp:**
- **GoEmotions [9]:** chỉ 457 trên 54.263 bình luận có dạng nào đó của "believe", và chỉ 15 bình luận dùng khung chủ ý như "choose to", "need to" hoặc "want to believe".
- **CommitmentBank [10]:** có 74 item với "believe", nhưng tất cả đều nằm dưới phủ định, câu hỏi, modal hoặc câu điều kiện. Chúng được chấm theo mức cam kết của người nói, không theo loại niềm tin.
- **EmpatheticDialogues [11]:** có 32 nhãn cảm xúc, trong đó có hopeful, faithful và anxious, nên có thể cung cấp mẫu tự nhiên. Nhưng số tình huống chứa "believe" vẫn chưa được đếm. Dữ liệu tự nhiên để sau tháng 5.

## 6. Metric

Với item $i$ và điều kiện $c$, gọi $m_{i,c}\in[0,1]$ là credence mà mô hình gán. Đó là câu trả lời dạng số chia cho 100, hoặc P(Yes) đã chuẩn hóa cho câu "thinks it is likely". Gọi $h_{i,c}$ là điểm trung bình của người, quy về $[0,1]$ như trong pilot/human.py. Vì đáp án chuẩn mực còn tranh cãi, ba metric chính được định nghĩa tương đối so với người ở mọi chỗ có thể.

**Thổi phồng credence (credence inflation, CI).** Báo cáo riêng cho item gián tiếp và item tự hiện thực hóa.

$$\mathrm{CI}=\frac{1}{N}\sum_{i}\Big[(m_{i,\mathrm{VD}}-m_{i,\mathrm{IR}})-(h_{i,\mathrm{VD}}-h_{i,\mathrm{IR}})\Big]$$

Bằng 0 nghĩa là khi thêm câu stake, mô hình dịch credence đúng bằng mức người dịch. Dương nghĩa là mô hình dịch nhiều hơn. Riêng vế của mô hình trong pilot là +0.44 với Qwen2.5-7B.

**Sai số so với credence được nêu (stated-credence error, SCE).** Metric này không cần chuẩn người.

$$\mathrm{SCE}=\frac{1}{N}\sum_{i}\big(\hat c_{i}-s_{i}\big)$$

Trong đó $\hat c_i$ là credence mà mô hình gán ở VD-K, và $s_i$ là credence mà văn bản nêu. Báo cáo kèm tỷ lệ item VD-K mà mô hình trả lời Yes cho câu "thinks it is likely". Đánh giá của người ở VD-K dùng để kiểm tra rằng người đọc chấp nhận con số được nêu.

**Mức khớp với người (human alignment, HA).**

$$\mathrm{HA}=\frac{\rho(m,h)}{\rho^{*}},\qquad \rho^{*}=\frac{2r}{1+r}$$

Trong đó:
- $\rho$ là tương quan Spearman trên các ô item × điều kiện, tính riêng cho từng thước đo rồi lấy trung bình;
- $r$ là tương quan giữa hai nửa ngẫu nhiên của nhóm người đánh giá;
- vì vậy $\rho^{*}$ là trần nhiễu (noise ceiling) của người.

Đi kèm ba metric chính là ba chỉ số chẩn đoán.

**Độ nhạy với cảm xúc**, với $e\in\{\mathrm{H},\mathrm{F}\}$, tính ở cả các ô có stake và không có stake:

$$\mathrm{ES}_{e}=\big(\bar m_{\mathrm{VD}\text{-}e}-\bar m_{\mathrm{VD}}\big)-\big(\bar h_{\mathrm{VD}\text{-}e}-\bar h_{\mathrm{VD}}\big)$$

**Khoảng chênh signature** là $\Delta_c=\log P(\text{thinks}\mid c)-\log P(\text{believes}\mid c)$. Nếu mô hình theo đúng khuôn mẫu của người [4] thì $\Delta_{\mathrm{TS}}>\Delta_{\mathrm{VD}}$.

**Khoảng chênh tường minh / ngầm** là độ chính xác của câu phân loại tường minh, trừ đi mức trùng với đa số người ở câu hỏi credence. Một mô hình gọi đúng tên cách đọc VD nhưng vẫn gán credence cao là mô hình có thông tin mà không dùng. Đó chính là lý do về mặt hành vi để làm §7.

Độ bền được báo cáo qua phương sai giữa các cách diễn đạt, và qua kết quả trên các miền giữ lại (held-out). Hiệu ứng ở người được kiểm định bằng mô hình hỗn hợp (mixed-effects), với hiệu ứng ngẫu nhiên cho người tham gia và cho item. Các so sánh trên mô hình giữ kiểm định cặp theo item và khoảng tin cậy bootstrap như trong pilot/analyze.py.

## 7. Định vị hiệu ứng

Đầu ra nên là một bản đồ theo layer và vị trí token, không phải một layer duy nhất. Các hiệu ứng kiểu này thường trải qua nhiều layer và attention head.

**Mô hình.** Cần hai mô hình mở từ 7B trở lên, vì Steele et al. [8] thấy khả năng theo dõi belief thất bại ở 3B.
- Qwen2.5-7B-Instruct, để nối tiếp pilot.
- Llama-3.1-8B-Instruct, vì có SAE huấn luyện sẵn cho bản base (Llama Scope, note.md §6.1).

Cả hai chạy ở bf16 bằng PyTorch với nnsight hoặc pyvene, trên Colab Pro, hoặc trên NDIF nếu NDIF có host mô hình đó (note.md §6.1).

**Phân tích gồm bốn bước, rẻ nhất trước:**

1. **Logit lens.** Theo dõi hiệu logit Yes trừ No qua các layer, để thấy câu trả lời VD và IR tách nhau từ layer nào.
2. **Activation patching.** Các minimal pair IR/VD chỉ khác nhau ở câu stake. Vì vậy, patching theo layer và vị trí (các token của câu stake, "believes", token cuối) đo được mỗi lần patch khôi phục bao nhiêu phần chênh lệch P(Yes) [12]. Attribution patching [13] dùng để quét nhanh, patching chính xác để xác nhận, rồi path patching thu hẹp kết quả xuống mức attention head.
3. **Probe tuyến tính.** Probe ở từng layer cho xác suất được nêu, và cho việc có hay không có câu stake. Dùng control task [14] và baseline bag-of-words. Nếu cả hai đều giải mã được tại các layer nơi câu stake đi vào câu trả lời, bằng chứng nghiêng về gộp ở mức đọc ra.
4. **DAS (distributed alignment search) [15].** Tìm một không gian con hạng thấp mang credence được gán tại các layer đó. Interchange intervention kiểm tra xem thay đổi biến cách đọc có làm credence đọc ra thay đổi theo không. Gộp ở mức biểu diễn dự đoán rằng hai biến này không tách được.

Nhánh này có thể bắt đầu từ tháng 11 trên 24 item của pilot, trước khi có dữ liệu người. Lý do là nó hỏi mô hình tính ra câu trả lời như thế nào, chứ không hỏi câu trả lời có đúng không.

## 8. Nếu có khoảng chênh: can thiệp

Đặt một mô hình BERT vào thay một layer sẽ không chạy được như mô tả, vì ba lý do:
- BERT có tokenizer và không gian embedding riêng, với kích thước ẩn 768. Trong khi đó Qwen2.5-7B là 3.584 và Llama-3.1-8B là 4.096.
- Mỗi layer transformer tính rất nhiều đặc trưng không liên quan đến belief, nên thay một layer sẽ làm hỏng mô hình trên diện rộng.
- Layer nơi causal tracing định vị được hiệu ứng thường không phải layer mà chỉnh sửa ở đó hiệu quả nhất [16].

Dù vậy, cốt lõi của ý tưởng là hợp lý. Chèn một module nhỏ đã huấn luyện vào đúng vị trí đã định vị là việc đã có dạng chuẩn.

**Phương pháp chính: ReFT (LoReFT) [17].** ReFT huấn luyện một can thiệp hạng thấp trên hidden state tại các layer và vị trí được chọn. Với hạng 4 trên residual stream 4.096 chiều, mỗi vị trí chỉ khoảng 33 nghìn tham số. Can thiệp được huấn luyện trên mục tiêu lấy từ chuẩn người ở một số miền. Sau đó kiểm tra trên các miền giữ lại, các item bi quan phòng vệ và hai bộ test bên ngoài. Bortoletto et al. [18] đã sửa được các suy luận ToM sai bằng chỉnh sửa activation có mục tiêu, nên cách làm này đã có tiền lệ cho việc gán belief.

**Ba baseline:**
- Activation steering tại cùng các layer [19].
- LoRA giới hạn ở các layer đã định vị, so với LoRA trên mọi layer và trên các layer ngẫu nhiên. So sánh này biến nhận định về định vị thành một phép thử [16].
- Một prompt yêu cầu mô hình tách credence khỏi thái độ.

**BERT vẫn có hai vai trò.**
- Một encoder nhỏ được fine-tune để phân loại cách đọc từ ngữ cảnh là baseline chỉ dùng văn bản. Nó cho thấy thông tin có sẵn trong văn bản.
- Chính bộ phân loại đó có thể làm router, chỉ bật steering ở ngữ cảnh VD. Cách này cùng tinh thần với conditional activation steering [20], vốn chỉ áp một vector steering khi input khớp một điều kiện.

Transcoder [21] là các bản thay thế thưa được huấn luyện cho layer MLP. Đây là dạng hiện có gần nhất với ý "thay một layer". Nhưng transcoder được làm để diễn giải chứ không phải để sửa, và chỉ đáng dùng nếu đã có sẵn cho mô hình được chọn.

Bất kỳ cách sửa nào cũng phải thỏa ba điều kiện:
- giữ credence ở TS vẫn cao;
- không làm giảm kết quả trên bài false-belief thông thường (BigToM [22]) và năng lực chung;
- cải thiện CI, SCE và HA trên dữ liệu giữ lại.

## 9. Phạm vi, mốc quyết định và lịch

Ở đây, benchmark và nghiên cứu khoa học xã hội là một bài. Chuẩn người, việc cho mô hình lặp lại [4] và [7], và hiệu ứng cảm xúc ở người đều là kết quả khoa học xã hội. Metric của benchmark được định nghĩa dựa trên chính các kết quả đó.

Các đóng góp dự kiến:
1. Một benchmark có chuẩn người, với biến cảm xúc và các metric ở trên.
2. Đánh giá trên nhiều mô hình.
3. Cho mô hình lặp lại hai nghiên cứu trên người đã công bố.
4. Định vị trong hai mô hình.
5. Một can thiệp, nếu Mốc 2 cho thấy có khoảng chênh.

Nếu muốn một bài thuần khoa học xã hội thì bỏ (4) và (5), và nhắm CogSci hoặc một tạp chí.

**Mốc 1, cuối tháng 10.** Thu đường chuẩn 9 người như dự định, bằng form hiện có. Nếu người cũng nói rằng người tin kiểu VD nghĩ p có khả năng cao, thì cách đặt vấn đề collapse phải đổi. Khi đó bài trở thành phép thử xem mô hình có tái tạo khuôn mẫu đọc của người không, với cảm xúc là thao tác chính. Nửa can thiệp nhiều khả năng sẽ bị bỏ.

Lưu ý về IRB: đánh giá của người dự định công bố thường cần được hội đồng đạo đức duyệt trước khi thu. Vì vậy nên coi vòng 9 người là kiểm tra nội bộ cho stimuli, và nộp hồ sơ IRB cho nghiên cứu thu chuẩn đầy đủ ngay trong tháng 10.

**Mốc 2, giữa tháng 2.** Chuẩn người đầy đủ và kết quả chạy mô hình có cho thấy khoảng chênh giữa mô hình và người ở CI hoặc SCE không? Nếu có, làm §8. Nếu không, bài báo cáo mức khớp, cùng với cách mô hình tính credence được gán.

**Mốc 3, giữa tháng 3.** Chọn venue theo những gì đã sẵn sàng.

| Tháng | Nhánh A: benchmark và nghiên cứu trên người | Nhánh B: cơ chế |
|---|---|---|
| 10 | Mốc 1; nộp IRB; tải stimuli từ OSF; chạy mô hình trên [4] và [7] | Chạy lại pilot ở bf16 bằng PyTorch |
| 11 | Viết và kiểm định item bản 2; mở rộng harness (credence dạng số, signature, mô hình API) | Logit lens và patching trên item của pilot |
| 12 đến 1 | Thu chuẩn trên Prolific; chạy toàn bộ mô hình | Probe; patching trên item bản 2 |
| 2 | Phân tích; Mốc 2 | DAS |
| 3 | Mốc 3; ablation | ReFT, steering và LoRA theo layer đã định vị, nếu có khoảng chênh |
| 4 | Viết bài; dataset card và công bố dữ liệu | Viết bài |
| 5 | Nộp bài | Nộp bài |

Nếu có hai người thì mỗi người phụ trách một nhánh là cách chia tự nhiên.

## 10. Venue

Lịch năm 2027 chưa được công bố, nên lịch năm 2026 là căn cứ tốt nhất [23].

| Venue | Hạn năm 2026 | Phù hợp với |
|---|---|---|
| NeurIPS, track Evaluations & Datasets | abstract 4/5, bài 6/5 | Bài đặt benchmark lên trước. Track đổi tên từ Datasets & Benchmarks năm 2026. Nhận benchmark mới, phương pháp đánh giá, nghiên cứu lấy con người làm trung tâm và kết quả âm tính. Yêu cầu host dữ liệu trên nền tảng như Hugging Face, kèm metadata Croissant |
| ACL Rolling Review, chu kỳ tháng 5 (cho EMNLP) | 25/5 | Bài đặt phát hiện lên trước, viết cho cộng đồng NLP và ngôn ngữ học |
| Workshop Mechanistic Interpretability tại ICML | 8/5 | Phần định vị và can thiệp. Non-archival, 4 hoặc 8 trang, nên có thể đi kèm một bài archival nếu quy định nộp trùng của venue kia cho phép |
| CogSci | 2/2 | Chỉ dành cho phiên bản thuần khoa học xã hội |

Hướng đề xuất là NeurIPS Evaluations & Datasets nếu Mốc 2 thuận lợi, đồng thời gửi phần mechanistic tới workshop ICML. Nếu bài chưa kịp hạn đầu tháng 5, thì chu kỳ ARR tháng 5 muộn hơn khoảng ba tuần.

## 11. Ngân sách

- Thu chuẩn người: khoảng $760.
- Chạy API: $30 đến $100 (theo note.md §6.0).
- GPU: $75 đến $150 (theo note.md §6.0).

Tổng khoảng $870 đến $1.010, gần mức thấp của ước tính giai đoạn 1 trong note ($900 đến $1.500).

## 12. Hai tuần tới

1. Thu đường chuẩn 9 người bằng form hiện có, coi là kiểm tra nội bộ.
2. Nộp hồ sơ IRB cho nghiên cứu thu chuẩn đầy đủ.
3. Tải stimuli từ OSF của [4] và [7], rồi chạy các mô hình của pilot trên đó bằng pilot/run.py.
4. Viết lại pilot/stimuli.py theo tám điều kiện, và theo cách chia stake gián tiếp / tự hiện thực hóa.
5. Chạy lại pilot Qwen2.5-7B ở bf16 bằng PyTorch, và làm lượt patching đầu tiên theo layer và vị trí.
6. Cập nhật README.md và note.md §0, §8 theo phạm vi mới.

## 13. Bản nháp abstract

Giữ bằng tiếng Anh vì sẽ dùng trực tiếp trong bài, giống cách note.md §4 đang làm.

> Evaluations of belief attribution in language models almost always use beliefs that track evidence. The verb "believe" also reports value-driven belief. A patient told that her surgery succeeds one time in ten may believe it will succeed because patients who believe recover better, while her credence stays low. Holding the sentence "X believes that p" fixed and varying only its context, we ask whether models attribute to X the credence and belief profile that human readers do. We introduce [NAME], a benchmark of [N] items crossing evidence, the practical stake of believing, the believer's emotion and an explicitly stated credence, normed by [N] human raters, with human-relative metrics for credence inflation, stated-credence error and alignment. Across [K] models, [finding]. We also replicate two published human studies of belief attribution with models, and we localize the attribution of credence in [models] with activation patching and distributed alignment search. Finally, we [show that a low-rank intervention at the localized layers closes the gap / characterize the mechanism].

## Tài liệu tham khảo

[1] Kunda, Z. (1990). The case for motivated reasoning. Psychological Bulletin, 108(3), 480-498.

[2] Lerner, J. S., and Keltner, D. (2001). Fear, anger, and risk. Journal of Personality and Social Psychology, 81(1), 146-159.

[3] Krizan, Z., and Windschitl, P. D. (2007). The influence of outcome desirability on optimism. Psychological Bulletin, 133(1), 95-121.

[4] Vesga, A., Van Leeuwen, N., and Lombrozo, T. (2025). Evidence for multiple kinds of belief in theory of mind. Journal of Experimental Psychology: General. Stimuli và dữ liệu: OSF project 38YGN.

[5] Yongsatianchot, N., and Marsella, S. (2025). Investigating motivated inference in large language models. Proceedings of the 9th Widening NLP Workshop (WiNLP). Code công bố với tên WishfulEval.

[6] Norem, J. K., and Cantor, N. (1986). Defensive pessimism: Harnessing anxiety as motivation. Journal of Personality and Social Psychology, 51(6), 1208-1217.

[7] Cusimano, C., and Lombrozo, T. (2021). Morality justifies motivated reasoning in the folk ethics of belief. Cognition, 209, 104513. Stimuli và dữ liệu có trên OSF.

[8] Steele, Wen, and Han (2026). One mechanism for many mental spaces, arXiv 2607.10248; và Belief-reality separation lives in routing, arXiv 2607.11945. Corpus và code: osteele/mental-spaces.

[9] Demszky, D., et al. (2020). GoEmotions: A dataset of fine-grained emotions. ACL 2020.

[10] de Marneffe, M.-C., Simons, M., and Tonhauser, J. (2019). The CommitmentBank: Investigating projection in naturally occurring discourse. Sinn und Bedeutung 23.

[11] Rashkin, H., Smith, E. M., Li, M., and Boureau, Y.-L. (2019). Towards empathetic open-domain conversation models: A new benchmark and dataset. ACL 2019.

[12] Meng, K., Bau, D., Andonian, A., and Belinkov, Y. (2022). Locating and editing factual associations in GPT. NeurIPS 2022.

[13] Syed, A., Rager, C., and Conmy, A. (2023). Attribution patching outperforms automated circuit discovery. arXiv 2310.10348.

[14] Hewitt, J., and Liang, P. (2019). Designing and interpreting probes with control tasks. EMNLP 2019.

[15] Geiger, A., Wu, Z., Potts, C., Icard, T., and Goodman, N. (2024). Finding alignments between interpretable causal variables and distributed neural representations. CLeaR 2024.

[16] Hase, P., Bansal, M., Kim, B., and Ghandeharioun, A. (2023). Does localization inform editing? Surprising differences in causality-based localization vs. knowledge editing in language models. NeurIPS 2023.

[17] Wu, Z., Arora, A., Wang, Z., Geiger, A., Jurafsky, D., Manning, C. D., and Potts, C. (2024). ReFT: Representation finetuning for language models. NeurIPS 2024.

[18] Bortoletto, M., et al. (2025). Brittle minds, fixable activations: Understanding belief representations in language models. Findings of EMNLP 2025; arXiv 2406.17513.

[19] Rimsky, N., et al. (2024). Steering Llama 2 via contrastive activation addition. ACL 2024.

[20] Lee, B. W., et al. (2025). Programming refusal with conditional activation steering. ICLR 2025; arXiv 2409.05907.

[21] Dunefsky, J., Chlenski, P., and Nanda, N. (2024). Transcoders find interpretable LLM feature circuits. NeurIPS 2024.

[22] Gandhi, K., Fränken, J.-P., Gerstenberg, T., and Goodman, N. D. (2023). Understanding social reasoning in language models with language models. NeurIPS 2023, Datasets and Benchmarks track.

[23] Trang lịch NeurIPS 2026 và call for papers của track Evaluations & Datasets; trang lịch ACL Rolling Review; call for papers của workshop Mechanistic Interpretability tại ICML 2026; trang hội nghị CogSci 2026. Tất cả truy cập ngày 27/9/2026.
