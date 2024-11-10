async function processQRCode(aula_id) {
    const response = await fetch('/process_qr', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ aula_id: aula_id })
    });
    const data = await response.json();
    if (data.status === 'success') {
        window.location.href = `/viewer?image_path=${encodeURIComponent(data.image_path)}`;
    } else {
        document.getElementById('result').innerText = 'Aula no encontrada.';
    }
}
