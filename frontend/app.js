async function fetchData(endpoint, elementId) {
  let url = "";

  if (endpoint === "/users") {
    url = "http://localhost:5001/users"; // Mapped port for user-service
  } else if (endpoint === "/products") {
    url = "http://localhost:5002/products"; // Mapped port for product-service
  } else if (endpoint === "/orders") {
    url = "http://localhost:5003/orders"; // Mapped port for order-service
  }

  try {
    const response = await fetch(url);
    const data = await response.json();
    document.getElementById(elementId).innerText = JSON.stringify(
      data,
      null,
      2
    );
  } catch (error) {
    console.error("Error fetching data:", error);
    document.getElementById(elementId).innerText = "Error fetching data";
  }
}
