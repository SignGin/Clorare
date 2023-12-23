import { Category, Gender, Season } from './enums';

export interface PostClothes {
  category: Category;
  cloth_type: string;
  season: Season;
  gender: Gender;
  image?: string | null;
}

export interface ErrorClothes {
  category: string;
  cloth_type: string;
  season: string;
  gender: string;
  image?: string;
}
