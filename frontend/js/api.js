// frontend/js/api.js
const API_BASE = "http://127.0.0.1:8000";

async function apiGet(endpoint) {
    try {

        const response = await fetch(
            `${API_BASE}${endpoint}`
        );

        if (!response.ok) {
            throw new Error(
                `HTTP Error ${response.status}`
            );
        }

        return await response.json();

    } catch (error) {

        console.error(error);

        return {
            error: error.message
        };
    }
}

async function apiPost(endpoint, body = {}) {

    try {

        const response = await fetch(
            `${API_BASE}${endpoint}`,
            {
                method: "POST",
                headers: {
                    "Content-Type":
                    "application/json"
                },
                body: JSON.stringify(body)
            }
        );

        return await response.json();

    } catch (error) {

        return {
            error: error.message
        };
    }
}

async function apiPatch(endpoint, body = {}) {

    try {

        const response = await fetch(
            `${API_BASE}${endpoint}`,
            {
                method: "PATCH",
                headers: {
                    "Content-Type":
                    "application/json"
                },
                body: JSON.stringify(body)
            }
        );

        return await response.json();

    } catch (error) {

        return {
            error: error.message
        };
    }
}