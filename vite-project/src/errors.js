export function ApiError(error) {
  if (error.response && error.response.status === 404) {
    window.location.href = '/404';
  }
}