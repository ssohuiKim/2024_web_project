import { writable } from 'svelte/store';

export const meetingInfo = writable([]);

// export const meetingInfo = writable({
//   meetingName: '',
//   categories: [],
//   startDate: '',
//   startTime: '',
//   endDate: '',
//   endTime: '',
//   applyDate: '',
//   location: '',
//   capacity: '',
//   details: ''
// });