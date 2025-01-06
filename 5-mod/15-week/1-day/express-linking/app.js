const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());

app.get('/', (req, res) => {
    return res.json({ message: 'Heyooo' });
});

app.get('/api/kahoots', (req, res) => {
    res.json({
        imageURLs: [
            'https://images-cdn.kahoot.it/61f18b15-fc9c-45e9-baab-0d402ede662f?auto=webp',

            'https://images-cdn.kahoot.it/e788f11a-7f13-4be8-ace3-79b241a5e48d?auto=webp',

            'https://images-cdn.kahoot.it/619bbd46-d42a-4f95-88fd-0b227e691550?auto=webp',

            'https://images-cdn.kahoot.it/91cd0c5c-bb2e-4875-a3ba-27f693969247?auto=webp',
        ],
    });
});

app.listen(3000, () => console.log('express is runninnnnnnn'));
