document.addEventListener("DOMContentLoaded", () => {
  const msg = "[partição 0 | offset 12] key='user123'  value='Testando envio ao Kafka'";
  document.getElementById("message").textContent = msg;
  console.log("Kafka message rendered:", msg);
});

