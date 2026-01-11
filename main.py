import cv2 as cv
import time


def main():
    video = cv.VideoCapture(0)

    if not video.isOpened():
        print("Error: Could not open webcam.")
        return

    frame_count = 0
    PROCESS_EVERY_N_FRAMES = 3

    prev_time = 0

    while True:
        ret, frame = video.read()
        if not ret:
            print("Error: Failed to read frame from webcam.")
            break

        # Resize frame for consistent processing & lower CPU usage
        frame = cv.resize(frame, (640, 480))

        frame_count += 1

        # Skip frames to control processing FPS
        if frame_count % PROCESS_EVERY_N_FRAMES != 0:
            continue

        # FPS calculation
        current_time = time.time()
        if prev_time == 0:
            prev_time = current_time
            continue

        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        # Display FPS on frame
        cv.putText(
            frame,
            f"FPS: {int(fps)}",
            (10, 40),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv.imshow("SMART ATTENDANCE - Camera Feed", frame)

        # Exit on 'q'
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
