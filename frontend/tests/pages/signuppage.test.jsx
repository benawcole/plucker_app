import { render, screen, act } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { vi } from "vitest";

import { useNavigate } from "react-router-dom";
import { SignUp } from "../../src/services/authentication";

import { SignUpPage } from "../../src/pages/SignUp";
// import { }

// Mocking React Router's useNavigate function
vi.mock("react-router-dom", () => {
  const navigateMock = vi.fn();
  const useNavigateMock = () => navigateMock; // Create a mock function for useNavigate
  const LinkMock = vi.fn();
  return { useNavigate: useNavigateMock, Link: LinkMock };
});

// Mocking the signup service
vi.mock("../../src/services/authentication", () => {
  const signupMock = vi.fn();
  return { SignUp: signupMock };
});

// Reusable function for filling out signup form
async function completeSignupForm() {
  const user = userEvent.setup();

  const userNameInputEl = screen.getByLabelText("Username:");
  const emailInputEl = screen.getByLabelText("Email:");
  const passwordInputEl = screen.getByLabelText("Password:");
  const confirmpasswordInputEl = screen.getByLabelText("Confirm Password:");
  const profileimageInputEl = screen.getByRole("profile-image");
  const submitButtonEl = screen.getByRole("submit-button");

  await user.type(userNameInputEl, "test");
  await user.type(emailInputEl, "test@email.com");
  await user.type(passwordInputEl, "1234");
  await user.type(confirmpasswordInputEl, "1234");

  await act(async () => {
    await user.click(profileimageInputEl, null);
    await user.click(submitButtonEl);
  });
}

describe("Signup Page", () => {
  beforeEach(() => {
    vi.resetAllMocks();
  });

  test.only("allows a user to signup", async () => {
    render(<SignUpPage />);

    await act(async () => {
        await completeSignupForm();
    })

    expect(SignUp).toHaveBeenCalledWith("test", "tester", "test@email.com", "1234");
  });

  test("navigates to /login on successful signup", async () => {
    render(<SignUpPage />);

    const navigateMock = useNavigate();

    await act(async () => {
      await completeSignupForm();
    })

    expect(navigateMock).toHaveBeenCalledWith("/");
  });

  test("navigates to /signup on unsuccessful signup", async () => {
    render(<SignUpPage />);

    SignUp.mockRejectedValue(new Error("Error signing up"));
    const navigateMock = useNavigate();

    await act(async () => {
      await completeSignupForm();
    })

    expect(navigateMock).toHaveBeenCalledWith("/");
  });


});
