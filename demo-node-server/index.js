const express = require("express");
const cors = require("cors");
const morgan = require("morgan");
const app = express();

app.use(express.json());
app.use(cors()); // 모든 도메인에 대해서 cores 허용
app.use(morgan("dev"));

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/sample", (req, res) => {
  const plusMinus = Math.floor(Math.random() * 10) % 2 === 0 ? -1 : 1;
  const temperatures = Math.floor(Math.random() * 50) * plusMinus;
  res.status(200).json({
    temperatures,
  });
});

app.post("/recommend", (req, res) => {
  console.log("req.body", req.body);
  res.status(201).json({
    comment: `따듯한 봄 날씨에 ${req.body.style}한 스타일을 원하는 당신에게 추천`,
    top: "맨투맨",
    pants: "청바지",
  });
});

const port = 3030;
app.listen(port, () => {
  console.log(`${port} 포트 번호로 서버가 실행되었습니다.`);
});
