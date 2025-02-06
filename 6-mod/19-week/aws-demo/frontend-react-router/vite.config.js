import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
        '/api': 'http://localhost:5000',
    }
}
})

// import { defineConfig } from 'vite';
// import react from '@vitejs/plugin-react';

// export default defineConfig({
//   plugins: [react()],
//   server: {
//     proxy: {
//       '/api': 'http://server:8000',
//     },
//     host: '0.0.0.0',
//     port: 5173,
//     // watch: {
//     //   usePolling: true,
//     // },
//   },
// });
