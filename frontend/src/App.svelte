<script>
    let words = "Привет";
    let speaker = "baya";
    let sample_rate = "48000";
    async function speak() {
        let result = await fetch(
            `/speak?words=${encodeURIComponent(words)}&speaker=${speaker}&sample_rate=${sample_rate}`
        );
        console.log(await result.json());
    }
    async function get_audio_file() {
        let url = `/get_audio_file?words=${encodeURIComponent(words)}&speaker=${speaker}&sample_rate=${sample_rate}`;
        const file = await fetch(url);
        const fileBlob = await file.blob();
        const fileURL = URL.createObjectURL(fileBlob);
        const anchor = document.createElement("a");
        anchor.href = fileURL;
        anchor.download = "audio.wav";
        document.body.appendChild(anchor);
        anchor.click();
        document.body.removeChild(anchor);
        URL.revokeObjectURL(fileURL);
    }
</script>

<!-- {words}
{speaker}
{sample_rate} -->

<form>
    <label for="">Слова</label>
    <textarea bind:value={words} />
    <label for="speaker">Голос</label>
    <select bind:value={speaker} name="speaker">
        <option>aidar</option>
        <option>baya</option>
        <option>kseniya</option>
        <option>xenia</option>
        <option>random</option>
    </select>
    <label for="sample_rate">Sample Rate, Hz</label>
    <select bind:value={sample_rate} name="sample_rate">
        <option>8000</option>
        <option>24000</option>
        <option>48000</option>
    </select>
</form>
<button on:click={speak}>Сказать</button> <button on:click={get_audio_file}>Скачать аудио</button>

<style>
    form {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    textarea {
        height: 120px;
        width: 300px;
    }
</style>
