// frontend/js/api.js
const API_BASE = "http://127.0.0.1:8000";

async function getData(endpoint) {
    try {
        const response = await fetch(
            `${API_BASE}${endpoint}`
        );

        if (!response.ok) {
            throw new Error(
                `HTTP ${response.status}`
            );
        }

        return await response.json();

    } catch(error) {

        console.error(error);

        return {
            error: error.message
        };
    }
}