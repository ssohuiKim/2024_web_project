<script>

    let title = '';
    let date = '';
    let content = '';
  
    function submitMeeting() {
        meetings.update(currentMeetings => {
            return [...currentMeetings, { title, date, content }];
        });
        title = '';
        date = '';
        content = '';
    }
  </script>
  
  <h2>모집글 쓰기</h2>
  <div class="form-container">
    <form on:submit|preventDefault={submitMeeting}>
      <div>
        <label for="title">제목</label>
        <input id="title" type="text" bind:value={title}>
      </div>
      <div>
        <label for="date">날짜</label>
        <input id="date" type="date" bind:value={date}>
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" bind:value={content}></textarea>
      </div>
      <button type="submit">등록하기</button>
    </form>
  </div>
  
  <style>
    .form-container {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
    max-width: 700px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-right: auto;
    margin-left: auto;
    }

    h2 {
        margin-top: 40px;
        margin-bottom: 30px;
        font-size: 20px;
        text-align: center;
    }

    form > div {
      display: flex;
      align-items: center;
      margin-bottom: 1rem;
    }

    label {
      margin-right: 10px;
    }
    #title{
        width: 93%;;
    }
    #date{
        width: 35%;
    }
    #content {
    width: 93%;
    height: 150px;
    box-sizing: border-box;
    }

    button {
    width: 100%;
    padding: 10px;
    border: none;
    background-color: orange;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-weight: bold;
    border-radius: 5px;
    }

    button:hover {
    background-color: grey; /* 마우스 오버시 버튼 색상을 변경합니다. */
    }

  </style>
    